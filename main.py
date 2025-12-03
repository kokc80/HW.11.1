import os

from src.generators import filter_by_currency
from src.processing import filter_by_state, process_bank_search, sort_by_date
from src.transaction_reader import read_trans_csv, read_trans_excel
from src.utils import read_json

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
trans_dict: list[dict]
filename = ""


def input_file_choice(inp_ch_1: str, filename_1) -> list[dict]:
    # функция для выбора файла
    if inp_ch_1 == "1":
        filename_1 = f"{ROOT_DIR}\\data\\{filename_1}"
        print(f"Для  обработки выбран JSON-файл: {filename_1}\n")
        if os.path.isfile(filename_1) and filename_1 != "":
            trans_dict_1 = read_json(filename_1)
        else:
            trans_dict_1 = []
        print(trans_dict_1)
        return trans_dict_1
    if inp_ch_1 == "2":
        filename_1 = f"{ROOT_DIR}\\data\\{filename_1}"
        print(f"Для обработки выбран CSV-файл: {filename_1}\n")
        if os.path.isfile(filename_1) and filename_1 != "":
            trans_dict_1 = read_trans_csv(filename_1)
            return trans_dict_1
    if inp_ch_1 == "3":
        filename_1 = f"{ROOT_DIR}\\data\\{filename_1}"
        print(f"Для обработки выбран XLSX-файл: {filename_1}\n")
        if os.path.isfile(filename_1):
            trans_dict_1 = read_trans_excel(filename_1)
            return trans_dict_1


def main():
    # отвечает за основную логику проекта и связывает функциональности между собой
    print(
        """Привет! Добро пожаловать в программу работы с банковскими транзакциями.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла
    """
    )
    user_choice_1 = 0
    user_choice_2 = "none"
    user_choice_3 = "none"
    user_choice_4 = "none"
    user_choice_5 = "none"
    user_choice_6 = "none"
    trans_dict: list[dict] = []

    while True:
        if user_choice_1 in ("1", "2", "3"):
            if user_choice_1 == "1":
                print("Для обработки выбран JSON-файл\n")
                filename_1 = "transactions.json"
                break
            if user_choice_1 == "2":
                print("Для обработки выбран CSV-файл\n")
                filename_1 = "transactions.csv"
                break
            if user_choice_1 == "3":
                print("Для обработки выбран XLSX-файл\n")
                filename_1 = "transactions_excel.xlsx"
                break
        else:
            user_choice_1 = input("Ваш выбор?\n")
    while True:
        if user_choice_1 in ("1", "2", "3"):
            trans_dict = input_file_choice(user_choice_1, filename_1)
            break
        else:
            user_choice_1 = input("Ваш выбор?\n")

    print(
        f"Введите статус, по которому необходимо выполнить фильтрацию. \n"
        f"Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
    )
    while True:
        if user_choice_2.lower() in ("executed", "canceled", "pending"):
            print(f'Операции отфильтрованы по статусу "{user_choice_2.upper()}"\n')
            trans_dict = filter_by_state(trans_dict, user_choice_2.upper())
            print(f"статус {trans_dict}")
            break
        if user_choice_2.lower() == "none":
            user_choice_2 = input("Ваш выбор? \n")
        else:
            print(f'Статус операции "{user_choice_2}" недоступен.')
            user_choice_2 = input("Ваш выбор? \n")

    print("Отсортировать операции по дате? Да/Нет\n")
    while True:
        if user_choice_3.lower() == "да":
            if user_choice_4 == "none":
                user_choice_4 = input("Отсортировать по возрастанию или по убыванию?\n")
            else:
                break
            while True:
                if user_choice_4.lower() == "по возрастанию":
                    trans_dict = sort_by_date(trans_dict, reverse1=False)
                    break
                if user_choice_4.lower() == "по убыванию":
                    trans_dict = sort_by_date(trans_dict, reverse1=True)
                    break
                else:
                    if user_choice_4.lower() not in ("по возрастанию", "по убыванию"):
                        user_choice_4 = input('Ваш выбор? "по возрастанию"\\"по убыванию"\n')
        else:
            if user_choice_3.lower() == "нет":
                break
            else:
                user_choice_3 = input('Ваш выбор? "Да"\\"Нет"\n')
        print(f"по дате {trans_dict}")

    user_choice_5 = input("Выводить только рублевые транзакции? Да / Нет\n")
    while True:
        if user_choice_5.lower() in ("да", "нет", "none"):
            if user_choice_5.lower() == "да":
                trans_dict = list(filter_by_currency(trans_dict, "RUB"))
                break
            if user_choice_5.lower() == "нет":
                trans_dict = trans_dict
                break
        else:
            user_choice_5 = input('Ваш выбор? "Да"\\"Нет"\n')
    print(f"RUB {trans_dict}")

    user_choice_6 = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n")
    while True:
        if user_choice_6.lower() in ("да", "нет", "none"):
            if user_choice_6 == "да":
                search_data = input("Введите слово для поиска: ")
                trans_dict = process_bank_search(trans_dict, search_data)
            break
        else:
            user_choice_6 = input('Ваш выбор? "Да"\\"Нет"\n')

    print("Распечатываю итоговый список транзакций...")
    print(trans_dict)


main()
