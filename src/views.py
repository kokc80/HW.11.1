import os
import os
import datetime
import math
import json
import requests
from numpy.ma.extras import unique

from src.transaction_reader import read_trans_excel
from src.utils import read_json

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def str_to_date(date_i: str, period_d="M") -> dict:
    """Функция для перевода строки в datetime
    возвращает словарь из даты начала и даты окончания"""
    date_ex1: datetime
    date_ex2: datetime
    if period_d == "ALL":
        date_ex1 = datetime.datetime.strptime("1950-01-01 00:00:01", "%Y-%m-%d %H:%M:%S")
        date_ex2 = datetime.datetime.strptime("2222-12-31 23:59:59", "%Y-%m-%d %H:%M:%S")
    else:
        date_ex2 = datetime.datetime.strptime(date_i, "%Y-%m-%d %H:%M:%S")
    if period_d == "W" and date_ex2.day <= 7:
        date_ex1 = date_ex2.replace(month=date_ex2.month, day=1, year=date_ex2.year, hour=0, minute=0, second=1)
    else:
        date_ex1 = date_ex2.replace(month=date_ex2.month, day=date_ex2.day - 7, year=date_ex2.year)
    if period_d == "M":
        date_ex1 = date_ex2.replace(month=date_ex2.month, day=1, year=date_ex2.year)
    if period_d == "Y":
        date_ex1 = date_ex2.replace(month=date_ex2.month, day=1, year=date_ex2.year - 1)
    if period_d == "ALL":
        date_ex1 = date_ex2.replace(month=date_ex2.month, day=1, year=1900)
    return {"Дата начала": date_ex1, "Дата окончания": date_ex2}


def read_sett(filename: str) -> list[dict]:
    settings_list = read_json(filename)
    return (settings_list)


def str_greeting(time_1: datetime) -> str:
    """Функция для вывода приветствия в зависимости от времени"""
    greeting_val: str = "none"
    if time_1.hour >= 6 and time_1.hour < 10 :
        greeting_val = "Доброе утро"
    if time_1.hour >= 10 and time_1.hour < 16 :
        greeting_val = "Добрый день"
    if time_1.hour >= 16 and time_1.hour <= 21 :
        greeting_val = "Добрый вечер"
    if time_1.hour >= 21 or (time_1.hour >= 0 and time_1.hour <= 6):
        greeting_val = "Доброй ночи"
    return (greeting_val)


def sort_by_sum(transact_list: list[dict]) -> list[dict]:
    """Сортировка по Сумме"""
    list_sorted = sorted(transact_list, key=lambda p: p["Сумма операции"], reverse=True)
    list_new = list_sorted[0:4:1]
    return (list_sorted)


def sp500(list_stocks: list) -> list:
    """Функция принимает список акций и возвращает список стоимости акций"""
    list_stock_price = []
    for item_stock in list_stocks:
        api_url = 'https://api.api-ninjas.com/v1/stockprice?ticker={}'.format(item_stock)
        response = requests.get(api_url, headers={'X-Api-Key': 'gGXKL/ZK0xeTUntTxi4iDw==OjDYqa02l4VIPlYW'})
        list_sp = {}
        if response.status_code == requests.codes.ok:
            stock_price = response.json()
            list_sp= (stock_price["ticker"], stock_price["price"])
            list_stock_price.append(list_sp)
            # лог print("response list_stock", response)
        else:
            print("Error:", response.status_code, response.text)
    return list_stock_price


def curr_rate(list_cur: list) -> list[dict]:
    api_url = "https://v6.exchangerate-api.com/v6/5d56c60cad06d1e4126e1e91/latest/RUB"
    response = requests.get(api_url)
    curr_val = response.json()
    print("response curr_rate",response)
    list_cur_f = curr_val["conversion_rates"]
    list_curs = []
    for item_c in list_cur:
        list_curs1 = (item_c, list_cur_f[item_c])
        list_curs.append(list_curs1)
    return (list_curs)

def main_web(date_input: str, period_d="ALL"):
    """Главная функция, принимающая на вход строку с датой и временем в формате
    YYYY-MM-DD HH:MM:SS и возвращающая JSON-ответ с данными:"""
    file_sett = ROOT_DIR + "\\data\\user_settings.json"
    print(file_sett)
    sett_list = read_sett(file_sett)
    list_curr = (sett_list[0]["user_currencies"])
    list_stocks = (sett_list[0]["user_stocks"])

    excel_data = read_trans_excel(ROOT_DIR + "\\data\\operations2.xlsx")
    all_card_numbers = []

    dates = str_to_date(date_input, period_d)
    list_top_excel = []
    list_top_excel = sort_by_sum(excel_data)[:5]
    list_top_transaction = []

    for transact in list_top_excel:
        new_transact = {"date": transact.get("Дата операции"), "amount": transact.get("Сумма операции"),
                        "category": transact.get("Категория"), "description": transact.get("Описание")}
        list_top_transaction.append(new_transact)

    for transaction in excel_data:
        if ("Номер карты" in transaction and "Сумма операции" in transaction and "Кэшбэк" in transaction):
            if transaction["Номер карты"] not in [None, " ", {}, [], ""]:
                card_num = str(transaction["Номер карты"])
                all_card_numbers.append(card_num)
        dedupl_card_list = list()
        [dedupl_card_list.append(item)
        for item in all_card_numbers if (item not in dedupl_card_list and item not in ['nan'])]

    new_dict = []
    date_1 = dates["Дата начала"]
    date_2 = dates["Дата окончания"]
    for trans in excel_data:
        date_3 = datetime.datetime.strptime(trans.get("Дата операции"), "%d.%m.%Y %H:%M:%S")
        if (date_3 >= date_1 and date_3 < date_2):
            last_digits = "0000"
            if trans["Номер карты"] in dedupl_card_list:
                last_digits = trans["Номер карты"]
                last_digits = last_digits[-4:]
            total_spent = trans.get("Сумма операции")
            if math.isnan(total_spent):
                total_spent = 0
            cashback = trans.get("Кэшбэк", 0)
            if math.isnan(cashback):
                cashback = 0
            date_oper = trans.get('Дата операции')
            new_dict_i = {"last_digit": last_digits, "cashback": cashback, "total_spent": total_spent,
                          "date_oper": date_oper}
            new_dict.append(new_dict_i)
    unique_card_list = list() # список номеров карт
    for item in new_dict:
        if item["last_digit"] not in unique_card_list:
            unique_card_list.append(item["last_digit"])

    trans_list_end = []
    for items in unique_card_list:
        total_spent = 0
        cashback = 0

        for trans in new_dict:
            if trans["last_digit"] == items:
                total_spent = total_spent + trans["total_spent"]
                cashback_1 = trans["cashback"]
                cashback = cashback + cashback_1
                trans_list_item = {"last_digit": items, "cashback": cashback, "total_spent": total_spent}
        trans_list_end.append(trans_list_item)
        # создать Json
    str_main = json.dumps(trans_list_end, ensure_ascii=False, indent=2)
    str_top = json.dumps(list_top_transaction, ensure_ascii=False, indent=2)

    time_now = datetime.datetime.now()
    greeting_val_g = str_greeting(time_now)

    list_out = [{"greting": greeting_val_g}]
    list_out_tmp = {"cards": trans_list_end}
    list_out.append(list_out_tmp)
    list_out_tmp = {"top_transaction": list_top_transaction}
    list_out.append(list_out_tmp)
    list_out_tmp = {"currency_rates": list_curr}
    list_out.append(list_out_tmp)
    list_out_tmp = sp500(list_stocks)
    list_out.append(list_out_tmp)
    json_out = json.dumps(list_out, ensure_ascii=False, indent=2)
    return (json_out)
