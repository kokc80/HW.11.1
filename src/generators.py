# trans_list = (
#     [
#         {
#         "id": 939719570,
#         "state": "EXECUTED",
#         "date": "2018-06-30T02:08:58.425572",
#         "operationAmount":
#             {
#             "amount": "9824.07",
#             "currency":
#                 {
#                 "name": "USD",
#                 "code": "USD"
#             }
#         },
#           "description": "Перевод организации",
#           "from": "Счет 75106830613657916952",
#           "to": "Счет 11776614605963066702"
#         },
#         {
#          "id": 142264268,
#          "state": "EXECUTED",
#          "date": "2019-04-04T23:20:05.206878",
#          "operationAmount":
#              {
#              "amount": "79114.93",
#              "currency":
#                  {
#                  "name": "USD",
#                  "code": "USD"
#                  }
#              },
#          "description": "Перевод со счета на счет",
#          "from": "Счет 19708645243227258542",
#          "to": "Счет 75651667383060284188"
#          },
#         {
#             "id": 1122000000,
#             "state": "EXECUTED",
#             "date": "2025-04-04T23:20:05.206878",
#             "operationAmount":
#                 {
#                     "amount": "79114.93",
#                     "currency":
#                         {
#                             "name": "RUR",
#                             "code": "RUR"
#                         }
#                 },
#             "description": "Перевод со счета на счет",
#             "from": "Счет 19708645243227258542",
#             "to": "Счет 75651667383060284188"
#         },
#         {
#             "id": 454545400000,
#             "state": "EXECUTED",
#             "date": "2025-04-04T23:20:05.206878",
#             "operationAmount":
#                 {
#                     "amount": "79114.93",
#                     "currency":
#                         {
#                             "name": "EUR",
#                             "code": "EUR"
#                         }
#                 },
#             "description": "Перевод со счета на счет",
#             "from": "Счет 19708645243227258542",
#             "to": "Счет 75651667383060284188"
#         }
#     ]
# )


def filter_by_currency(transact: list, currency: str):
    """принимает на вход список словарей, представляющих транзакции.
    Функция должна возвращать итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)."""
    for trans in transact:
        try:
            if trans["operationAmount"]["currency"]["name"] == currency:
                yield trans
        except KeyError:
            continue  # пропускаем некорректные транзакции


def transaction_descriptions(transact_1: list):
    """генератор принимает список словарей с транзакциями и возвращает описание
    каждой операции по очереди."""
    for trans_1 in transact_1:
        try:
            yield trans_1["description"]
        except KeyError:
            pass  # пропускаем транзакции без описания


def card_number_generator(num_1: int, num_2: int):
    """Генератор генерирует номера карт"""
    for num in range(num_1, num_2 + 1):
        yield ("{:04d} {:04d} {:04d} {:04d}".
               format(num // 10**12,
                      (num // 10**8) % 10**4, (num // 10**4) % 10**4,
                      num % 10**4))
