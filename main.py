import os

from src.external_api import convert_exchange_rate
from src.utils import read_json

ROOT_DIR = os.path.dirname(
    os.path.abspath(__file__)
)
transaction_dict: dict = []
file_path_data = f"{ROOT_DIR}\\data\\operations.json"
transaction_dict = read_json(file_path_data)
param_dict = transaction_dict[2]

if type(param_dict) is dict:
    # print(param_dict)
    print(convert_exchange_rate(param_dict))

tr_list = {
    "operationAmount": {
        "currency": {
            "code": "USD"
        },
        "amount": "100"
    }
}
