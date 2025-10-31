import requests
def convert_exchange_rate (money_from: str, money_to: str, money_amount:float) -> float:
    """Фуенкция для работы с API конвертация валюты"""
    url = (f"https://api.apilayer.com/exchangerates_data/convert?to="
           f"{money_to}&from={money_from}&money_amount={money_amount}")
    payload = {}
    headers= {
        "apikey": "Z1jrc2XlucP9tlgEg3gkcfXDQt0MuG19"
    }
    response = requests.request("GET", url, headers=headers, data = payload)
    status_code = response.status_code
    result = response.text


def transactions_amount(trans: list) -> float:
    """вывод суммы в руб"""
    if trans["operationAmount"]["currency"]["code"] == "RUB":
        return(trans["operationAmount"]["amount"])
    else:
        amount_rub=(float(trans["operationAmount"]["amount"])*
                    convert_exchange_rate(str(trans["operationAmount"]["currency"]["code"]),"RUB")*
                    trans["operationAmount"]["amount"])
        return(amount_rub)

