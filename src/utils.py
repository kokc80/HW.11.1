import os, json
from src.external_api import transactions_amount


def read_json (filename=None)->list:
    """чтение файла json"""
    print("путь "+filename)
    if os.path.isfile(filename):
        print("Файл существует")
        # Открываем файл и читаем строки
        with open(filename, encoding='utf-8') as f:
            json_list = json.load(f)
            if type(json_list) == list:
                return json_list
            else:
                return []
    else:
        return []


ROOT_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)
file_path_data=f"{ROOT_DIR}\\data\\operations.json"
transaction_lines = read_json(file_path_data)

print(transactions_amount(transaction_lines[2]))