import datetime
import os

import requests
from dotenv import load_dotenv

# Загрузка переменных из .env-файла
load_dotenv()

# Получение значения переменной GITHUB_TOKEN из .env-файла
api_key = os.getenv('API_KEY')


def convert_exchange_rate(tr_list: list) -> float:
    """Функция для работы с API формирует ссылку для работы с API и конвертирует валюту на выходе сумма в рублях"""
    if tr_list["operationAmount"]["currency"]["code"] == "RUB":
        return (float(tr_list["operationAmount"]["amount"]))
    else:
        money_to = "RUB"
        money_from = tr_list["operationAmount"]["currency"]["code"]
        money_amount = tr_list["operationAmount"]["amount"]
        date_oper = datetime.datetime.now().strftime("%Y-%m-%d")
        url = (f"https://api.apilayer.com/exchangerates_data/convert?to="
               f"{money_to}&from={money_from}&amount={money_amount}&date={date_oper}")
        headers = {"apikey": api_key}
        try:
            response = requests.request("GET", url, headers=headers)
            response.raise_for_status()  # Проверка статуса ответа
            data = response.json()
            # Проверка наличия ключа 'result'
            if 'result' in data:
                return data['result']
            else:
                print("Ключ 'result' отсутствует в ответе")
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP ошибка: {http_err}")
        except requests.exceptions.RequestException as err:
            print(f"Ошибка запроса: {err}")
        except ValueError as json_err:
            print(f"Ошибка парсинга JSON: {json_err}")
