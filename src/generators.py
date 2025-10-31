from typing import Iterable


def filter_by_currency(transact: list, currency: str) -> Iterable:
    """принимает на вход список словарей, представляющих транзакции.
    Функция должна возвращать итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)."""
    for trans in transact:
        try:
            if trans["operationAmount"]["currency"]["name"] == currency:
                yield trans
        except KeyError:
            continue  # пропускаем некорректные транзакции


def transaction_descriptions(transact_1: list) -> Iterable:
    """генератор принимает список словарей с транзакциями и возвращает описание
    каждой операции по очереди."""
    for trans_1 in transact_1:
        try:
            yield trans_1["description"]
        except KeyError:
            pass  # пропускаем транзакции без описания


def card_number_generator(num_1: int, num_2: int) -> Iterable:
    """Генератор генерирует номера карт"""
    for num in range(num_1, num_2 + 1):
        yield (
            "{:04d} {:04d} {:04d} {:04d}".format(
                num // 10**12, (num // 10**8) % 10**4, (num // 10**4) % 10**4, num % 10**4
            )
        )
