from src.external_api import convert_exchange_rate

test_res = 7493507.550329


def test_convert_exchange_rate():
    assert convert_exchange_rate('USD', 'RUB', 92688.46, '2025.11.02') == test_res
