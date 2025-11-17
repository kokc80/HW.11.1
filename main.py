import os
from src.processing import process_bank_search
from src.utils import read_json
from src.transaction_reader import read_trans_excel, read_trans_csv

ROOT_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

global trans_dict
trans_dict = []
filename = ""


def main():
    # отвечает за основную логику проекта и связывает функциональности между собой
    print("""Привет! Добро пожаловать в программу работы с банковскими транзакциями.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла
    """)
    user_choice_1 = 0
    user_choice_2 = "none"
    user_choice_3 = "none"
    user_choice_4 = "none"
    user_choice_5 = "none"
    transaction_dict = []
    while True:
        if user_choice_1 in ("1", "2", "3"):
            if user_choice_1 == "1":
                print("Для обработки выбран JSON-файл\n")
                filename = input("Введите название JSON файла: ")
                filename = "f{ROOT_DIR}\\data\\{filename}"
                if os.path.isfile(filename):
                    trans_dict = read_json(filename)
                break
            if user_choice_1 == "2":
                filename = input("Введите название CSV файла: ")  # transactions.csv
                filename = f"{ROOT_DIR}\\data\\{filename}"
                print(f"{filename}\n")
                if os.path.isfile(filename):
                    trans_dict = read_trans_csv(filename)
                print(f"{trans_dict}")
                print("Для обработки выбран CSV-файл\n")
                break
            if user_choice_1 == "3":
                filename = input("Введите название XLSX файла: ")
                filename = "f{ROOT_DIR}\\data\\{filename}"
                if os.path.isfile(filename):
                    trans_dict = read_trans_excel(filename)
                print("Для обработки выбран XLSX-файл\n")
                break
        else:
            user_choice_1 = input("Ваш выбор?\n")
    print("""Введите статус, по которому необходимо выполнить фильтрацию.
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
    while True:
        if user_choice_2.lower() in ("executed", "canceled", "pending", "none"):
            if user_choice_2.lower() == "executed":
                print("Операции отфильтрованы по статусу \"EXECUTED\"\n")
                break
            if user_choice_2.lower() == "canceled":
                print("Операции отфильтрованы по статусу \"CANCELED\"\n")
                break
            if user_choice_2.lower() == "pending":
                print("Операции отфильтрованы по статусу \"PENDING\"\n")
                break
            if user_choice_2.lower() == "none":
                user_choice_2 = input("Ваш выбор? \n")
        else:
            print(f"Статус операции \"{user_choice_2}\" недоступен.")
            user_choice_2 = input("Ваш выбор? \n")
    print("Отсортировать операции по дате? Да/Нет\n")
    while True:
        if user_choice_3.lower() in ("да", "нет"):
            break
        else:
            user_choice_3 = input("Ваш выбор? \"Да\"\\\"Нет\"\n")
    print("Отсортировать по возрастанию или по убыванию?\n")
    while True:
        if user_choice_4 in ("по возрастанию", "по убыванию"):
            break
        else:
            user_choice_4 = input("Ваш выбор? \"по возрастанию\"\\\"по убыванию\"\n")
    print("Выводить только рублевые транзакции? Да / Нет\n")
    while True:
        if user_choice_4.lower() in ("да", "нет", "none"):
            break
        else:
            user_choice_4 = input("Ваш выбор? \"Да\"\\\"Нет\"\n")
    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n")
    while True:
        if user_choice_5.lower() in ("да", "нет", "none"):
            break
        else:
            user_choice_5 = input("Ваш выбор? \"Да\"\\\"Нет\"\n")
    search_data = input("Введите слово для поиска: ")
    process_bank_search(transaction_dict, search_data)
    print("Распечатываю итоговый список транзакций...")


main()
