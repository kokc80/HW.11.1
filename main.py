import os, datetime
from src.external_api import convert_exchange_rate
from src.utils import read_json

date_now = datetime.datetime.now()

ROOT_DIR = os.path.dirname(
    os.path.abspath(__file__)
)
transaction_dict=[]
file_path_data = f"{ROOT_DIR}\\data\\operations.json"
transaction_dict = read_json(file_path_data)


tr_list = transaction_dict[2]
if tr_list["operationAmount"]["currency"]["code"] == "RUB":
    print("RUB")
else:
    print(convert_exchange_rate(tr_list["operationAmount"]["currency"]["code"], "RUB",
                                  float(tr_list["operationAmount"]["amount"]), date_now.strftime("%Y-%m-%d")))
