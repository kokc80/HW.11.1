import os
from src.processing import filter_by_state, sort_by_date, process_bank_search
from src.utils import read_json
from src.transaction_reader import read_trans_excel, read_trans_csv
from src.generators import filter_by_currency

ROOT_DIR = os.path.dirname(
    os.path.abspath(__file__)

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
    user_choice_6 = "none"
    trans_dict: List[dict] = []

    while True:
        if user_choice_1 in ("1", "2", "3"):
            if user_choice_1 == "1":
                print("Для обработки выбран JSON-файл\n")
                filename = input("Введите название JSON файла: ") # transactions.json
                filename =f"{ROOT_DIR}\\data\\{filename}"
                if (os.path.isfile(filename) and filename != ""):
                    print(filename)
                    trans_dict = read_json(filename)
                    break
            if user_choice_1 == "2":
                filename = input("Введите название CSV файла: ")  # transactions.csv
                filename = f"{ROOT_DIR}\\data\\{filename}"
                print(f"File name: {filename}\n")
                if (os.path.isfile(filename) and filename != ""):
                    trans_dict = read_trans_csv(filename)
                print("Для обработки выбран CSV-файл\n")
                break
            if user_choice_1 == "3":
                filename = input("Введите название XLSX файла: ") # transactions.xlsx
                filename = f"{ROOT_DIR}\\data\\{filename}"
                if os.path.isfile(filename):
                    trans_dict = read_trans_excel(filename)
                print("Для обработки выбран XLSX-файл\n")
                break
        else:
            user_choice_1 = input("Ваш выбор?\n")
    print("""Введите статус, по которому необходимо выполнить фильтрацию.
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
    while True:
        if user_choice_2.lower() in ("executed", "canceled", "pending"):
            print(f"Операции отфильтрованы по статусу \"{user_choice_2.upper()}\"\n")
            trans_dict = filter_by_state(trans_dict,user_choice_2.upper())
            break
        if user_choice_2.lower() == "none":
            user_choice_2 = input("Ваш выбор? \n")
        else:
            print(f"Статус операции \"{user_choice_2}\" недоступен.")
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
                    trans_dict = sort_by_date(trans_dict, reverse1 = False)
                    break
                if user_choice_4.lower() == "по убыванию":
                    trans_dict = sort_by_date(trans_dict, reverse1 = True)
                    break
                else:
                    if user_choice_4.lower() not in ("по возрастанию", "по убыванию"):
                        user_choice_4 = input("Ваш выбор? \"по возрастанию\"\\\"по убыванию\"\n")
        else:
            if user_choice_3.lower() == "нет":
                break
            else:
                user_choice_3 = input("Ваш выбор? \"Да\"\\\"Нет\"\n")
    print("Выводить только рублевые транзакции? Да / Нет\n")
    while True:
        user_choice_5 = input("Ваш выбор? \"Да\"\\\"Нет\"\n")
        if user_choice_5.lower() in ("да", "нет", "none"):
            if user_choice_5.lower() == "да":
                trans_dict = list(filter_by_currency(trans_dict, "RUB"))
            break
        else:
            user_choice_5 = input("Ваш выбор? \"Да\"\\\"Нет\"\n")


    user_choice_6 = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n")
    while True:
        if user_choice_6.lower() in ("да", "нет", "none"):
            if user_choice_6 == "да":
                search_data = input("Введите слово для поиска: ")
                trans_dict = process_bank_search(trans_dict, search_data)
            break
        else:
            user_choice_6 = input("Ваш выбор? \"Да\"\\\"Нет\"\n")

    print("Распечатываю итоговый список транзакций...")
    print(trans_dict)

main()
