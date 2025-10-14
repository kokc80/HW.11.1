import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import pytest

from src.generators import *



pytest.fixture
def fix_transact_1():
    fix_transact_1=[(
        [
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
    )]
#    return(fix_transact_1)


def test_filter_by_currency ():
    excepted_result=[(
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
            }
            )]
    result =  list[(filter_by_currency(fix_transact_1,"USD"))]
    assert result == excepted result


