import os
import requests
from dotenv import load_dotenv

# Загрузка переменных из .env-файла
load_dotenv()

# Получение значения переменной GITHUB_TOKEN из .env-файла
api_key = os.getenv('API_KEY')


def convert_exchange_rate(money_from: str, money_to: str, money_amount: float, date: str) -> float:
    """Функция для работы с API формирует ссылку для работы с API и конвертирует валюту на выходе сумма в рублях"""
    url = (f"https://api.apilayer.com/exchangerates_data/convert?to="
           f"{money_to}&from={money_from}&amount={money_amount}")
    print(f"URL {url}")
    print(api_key)
    payload = {}
    headers = {
        "apikey": api_key
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    response = requests.get(url)
    data = response.json()
    print(data)
    # status_code = response.status_code
    result = response.json()["result"]
    return result
