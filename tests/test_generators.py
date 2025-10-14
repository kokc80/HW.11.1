import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import pytest
#from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from src.generators import *


@pytest.fixture
def fix_transact_1():
    return [
        {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount":
            {
            "amount": "9824.07",
            "currency":
                {
                "name": "USD",
                "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount":
            {
            "amount": "79114.93",
            "currency":
                {
                "name": "USD",
                "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
        "id": 1122000000,
        "state": "EXECUTED",
        "date": "2025-04-04T23:20:05.206878",
        "operationAmount":
            {
            "amount": "79114.93",
            "currency":
                {
                "name": "RUR",
                "code": "RUR"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
        "id": 454545400000,
        "state": "EXECUTED",
        "date": "2025-04-04T23:20:05.206878",
        "operationAmount":
            {
            "amount": "79114.93",
            "currency":
                {
                "name": "EUR",
                "code": "EUR"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }
    ]
#    return(fix_transact_1)


def test_filter_by_currency (fix_transact_1):
    expected_result=[{"id": 939719570,"state": "EXECUTED","date": "2018-06-30T02:08:58.425572","operationAmount":
                    {"amount": "9824.07","currency":{"name": "USD","code": "USD"}},"description": "Перевод организации",
                     "from": "Счет 75106830613657916952","to": "Счет 11776614605963066702"},
                    {"id": 142264268,"state": "EXECUTED","date": "2019-04-04T23:20:05.206878","operationAmount":
                    {"amount": "79114.93","currency":{"name": "USD","code": "USD"}},"description": "Перевод со счета на счет",
                     "from": "Счет 19708645243227258542","to": "Счет 75651667383060284188"}]
    result = filter_by_currency(fix_transact_1,"USD")
    assert list(result) == expected_result


def test_card_number_generator():
    expected_result = ["0000 0000 0010 0001", "0000 0000 0010 0002", "0000 0000 0010 0003", "0000 0000 0010 0004",
                       "0000 0000 0010 0005", "0000 0000 0010 0006", "0000 0000 0010 0007", "0000 0000 0010 0008"]
    result_card = card_number_generator(100001, 100008)
    assert list(result_card) == expected_result


def test_transaction_descriptions (fix_transact_1):
    expected_result = ["Перевод организации", "Перевод со счета на счет", "Перевод со счета на счет","Перевод со счета на счет"]
    result_descr = transaction_descriptions (fix_transact_1)
    assert list(result_descr) == expected_result

