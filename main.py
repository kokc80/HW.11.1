import os, datetime
from src.external_api import convert_exchange_rate
from src.utils import read_json

date_now = datetime.datetime.now()

ROOT_DIR = os.path.dirname(
    os.path.abspath(__file__)
)
transaction_dict=[]
file_path_data = f"{ROOT_DIR}\\data\\operations.json"
# print(f"Путь {file_path_data}")
transaction_dict = read_json(file_path_data)
try:
    # print(f"tran list {transaction_dict}")
    tr_list = transaction_dict[0]
    if tr_list["operationAmount"]["currency"]["code"] == "RUB":
        print("RUB")
        print(tr_list["operationAmount"]["amount"])
    else:
        print(convert_exchange_rate(tr_list["operationAmount"]["currency"]["code"], "RUB",
                                  float(tr_list["operationAmount"]["amount"]), date_now.strftime("%Y-%m-%d")))
except:
    print('Непредвиденная ошибка')