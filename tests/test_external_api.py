import datetime
from unittest.mock import Mock, patch

from src.external_api import convert_exchange_rate

# Допустим, что у нас есть `api_key`
api_key = 'NTP0jsKdybTUyjG8QerQGzzRft0fiuhc'


# Здесь мы определяем функцию теста
@patch('requests.request')
def test_convert_exchange_rate(mock_request):
    # Функкция тестирования Подготавливаем данные для теста
    tr_list = {
        "operationAmount": {
            "currency": {
                "code": "USD"
            },
            "amount": "100"
        }
    }

    # Подготовка mock ответа
    mock_response = Mock()
    mock_response.raise_for_status = Mock()
    mock_response.json.return_value = {'result': 7000}  # Предположим, что 100 USD = 7000 RUB
    mock_request.return_value = mock_response

    # Вызов функции и проверка результата
    result = convert_exchange_rate(tr_list)
    assert result == 7000, "Test failed: expected 7000"

    # Проверка, что mock_request был вызван с правильными параметрами
    money_to = "RUB"
    money_from = tr_list["operationAmount"]["currency"]["code"]
    money_amount = tr_list["operationAmount"]["amount"]
    date_oper = datetime.datetime.now().strftime("%Y-%m-%d")
    expected_url = (
        f"https://api.apilayer.com/exchangerates_data/convert?to="
        f"{money_to}&from={money_from}&amount={money_amount}&date={date_oper}"
    )

    mock_request.assert_called_once_with("GET", expected_url, headers={"apikey": api_key})


# Запуск теста
if __name__ == "__main__":
    test_convert_exchange_rate()
