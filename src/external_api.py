import os
import requests
import datetime
from dotenv import load_dotenv

# Загрузка переменных из .env-файла
load_dotenv()

# Получение значения переменной GITHUB_TOKEN из .env-файла
api_key = os.getenv('API_KEY')


def convert_exchange_rate(money_from: str, money_to: str, money_amount: float, date: str) -> float:
    """Функция для работы с API формирует ссылку для работы с API и конвертирует валюту на выходе сумма в рублях"""
    url = (f"https://api.apilayer.com/exchangerates_data/convert?to="
           f"{money_to}&from={money_from}&amount={money_amount}")
    # print(f"URL {url}")
    # print(api_key)
    payload = {}
    headers = {
        "apikey": api_key
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    # status_code = response.status_code
    result = response.json()["result"]
    return result


def transactions_amount(trans: list) -> float:
    """формирование данных для API конвертации с получением данных из API или возврата суммы в рублях"""
    date_now = datetime.datetime.now()
    if trans["operationAmount"]["currency"]["code"] == "RUB":
        return (trans["operationAmount"]["amount"])
    else:
        return convert_exchange_rate(trans["operationAmount"]["currency"]["code"], "RUB",
                              float(trans["operationAmount"]["amount"]), date_now.strftime("%Y-%m-%d"))
