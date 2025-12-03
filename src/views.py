import datetime
import json
import math
from pathlib import Path

import requests

from src.transaction_reader import read_trans_excel
from src.utils import read_json


def read_sett(filename: str) -> list[dict]:
    """чтение пользовательских данных"""
    settings_list = read_json(filename)
    return (settings_list)


def str_greeting() -> str:
    """Функция для вывода приветствия в зависимости от времени"""
    greeting_val: str = "none"
    time_1 = datetime.datetime.now()
    if time_1.hour >= 6 and time_1.hour < 10 :
        greeting_val = "Доброе утро"
    if time_1.hour >= 10 and time_1.hour < 16 :
        greeting_val = "Добрый день"
    if time_1.hour >= 16 and time_1.hour <= 21 :
        greeting_val = "Добрый вечер"
    if time_1.hour >= 21 or (time_1.hour >= 0 and time_1.hour <= 6):
        greeting_val = "Доброй ночи"
    return (greeting_val)


def unique_card_list(tr_data: list[dict], unique_col) -> list:
    unique_list = []
    # print(tr_data)
    for item in tr_data:
        if item[unique_col] not in unique_list:
            unique_list.append(item[unique_col])
    return unique_list


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
        date_ex2 = datetime.datetime.now()
    return {"Дата начала": date_ex1, "Дата окончания": date_ex2}


def card_maker(tr_data: list[dict], date: datetime, period="All") -> str:
    dates = str_to_date(date, period)
    date_1 = dates["Дата начала"]
    date_2 = dates["Дата окончания"]
    card_list = unique_card_list(tr_data, "Номер карты")
    new_cl = []
    for trans in tr_data:
        date_3 = datetime.datetime.strptime(trans.get("Дата операции"), "%d.%m.%Y %H:%M:%S")
        if (date_3 >= date_1 and date_3 < date_2):
            last_digits = str(trans["Номер карты"])
            total_spent = trans.get("Сумма операции")
            if math.isnan(total_spent):
                total_spent = 0
            cashback = trans.get("Кэшбэк", 0)
            if math.isnan(cashback):
                cashback = 0
            date_oper = trans.get('Дата операции')
            new_dict_i = {"last_digit": last_digits, "cashback": cashback, "total_spent": total_spent,
                          "date_oper": date_oper}
            new_cl.append(new_dict_i)
    trans_list_end = []
    for items in card_list:
        total_spent = 0
        cashback = 0
        trans_list_item = {}
        for trans in new_cl:
            if trans["last_digit"] == items:
                total_spent = total_spent + trans["total_spent"]
                cashback_1 = trans["cashback"]
                cashback = cashback + cashback_1
                trans_list_item = {"last_digit": items, "cashback": cashback, "total_spent": total_spent}
        trans_list_end.append(trans_list_item)
    return trans_list_end


def sort_by_sum(transact_list: list[dict]) -> list[dict]:
    """Сортировка по Сумме"""
    list_sorted = sorted(transact_list, key=lambda p: p["Сумма операции"], reverse=True)
    list_new = list_sorted[0:5:1]
    return (list_new)


def top_trans(data_ld: list[dict]) -> list[dict]:
    list_top_excel = sort_by_sum(data_ld)[:5]
    list_top_transaction = []
    for transact in list_top_excel:
        new_transact = {"date": transact.get("Дата операции"), "amount": transact.get("Сумма операции"),
                        "category": transact.get("Категория"), "description": transact.get("Описание")}
        list_top_transaction.append(new_transact)
    return (list_top_transaction)


def curr_rate(list_cur: list) -> list[dict]:
    api_url = "https://v6.exchangerate-api.com/v6/5d56c60cad06d1e4126e1e91/latest/RUB"
    response = requests.get(api_url)
    curr_val = response.json()
    # print("response curr_rate",response)
    list_cur_f = curr_val["conversion_rates"]
    list_curs = []
    for item_c in list_cur:
        list_curs1 = (item_c, list_cur_f[item_c])
        list_curs.append(list_curs1)
    return (list_curs)


def sp500(list_stocks: list) -> list:
    """Функция принимает список акций и возвращает список стоимости акций"""
    list_stock_price = []
    for item_stock in list_stocks:
        api_url = 'https://api.api-ninjas.com/v1/stockprice?ticker={}'.format(item_stock)
        response = requests.get(api_url, headers={'X-Api-Key': 'gGXKL/ZK0xeTUntTxi4iDw==OjDYqa02l4VIPlYW'})
        list_sp = {}
        if response.status_code == requests.codes.ok:
            stock_price = response.json()
            list_sp = (stock_price["ticker"], stock_price["price"])
            list_stock_price.append(list_sp)
            # лог print("response list_stock", response)
        else:
            print("Error:", response.status_code, response.text)
    return list_stock_price


def main_web(date_input: str, period_d="ALL"):
    BASE_DIR = Path(__file__).resolve().parent.parent
    file_sett = BASE_DIR.joinpath('data', 'user_settings.json')
    sett_list = read_sett(file_sett)
    list_curr = curr_rate(sett_list[0]["user_currencies"])
    list_stocks = (sett_list[0]["user_stocks"])
    excel_data_ld = read_trans_excel(file_main)
    list_top_transaction = top_trans(excel_data_ld)
    val_out = []
    greeting_val = str_greeting()
    val_out_tmp = {"greting": greeting_val}
    val_out.append(val_out_tmp)
    val_out_tmp = {"card": card_maker(excel_data_ld, date_input, period_d)}
    val_out.append(val_out_tmp)
    val_out_tmp = {"top_transaction": list_top_transaction}
    val_out.append(val_out_tmp)
    val_out_tmp = {"currency_rates": list_curr}
    val_out.append(val_out_tmp)
    val_out_tmp = sp500(list_stocks)
    val_out.append(val_out_tmp)
    json_out = json.dumps(val_out, ensure_ascii=False, indent=2)

    return (json_out)


BASE_DIR = Path(__file__).resolve().parent.parent
file_sett = BASE_DIR.joinpath('data', 'user_settings.json')
file_main = BASE_DIR.joinpath('data', 'operations1.xlsx')
# print(BASE_DIR, file_sett)
print(main_web("2021-09-27 20:56:30", period_d="ALL"))
