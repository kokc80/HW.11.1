import os
import json
from src.external_api import transactions_amount


def read_json(filename=None) -> list:
    """чтение файла json"""
    # print("путь " + filename)
    if os.path.isfile(filename):
        # Открываем файл и читаем строки
        with open(filename, encoding='utf-8') as f:
            json_list = json.load(f)
            if type(json_list) is list:
                return json_list
            else:
                return ""
    else:
        return ""


ROOT_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)
file_path_data = f"{ROOT_DIR}\\data\\operations_test.json"
transaction_lines = read_json(file_path_data)

tr_list = transaction_lines[0]
# print(f"Transaction{tr_list}")
print(transactions_amount(tr_list))
