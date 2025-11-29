import datetime
import pandas as pd
import os
from src.transaction_reader import read_trans_excel
from dateutil.relativedelta import relativedelta


def spending_by_category(transactions_df: pd.DataFrame, category: str, date:str = None) -> pd.DataFrame:
    """Функция возвращает траты по заданной категории за последние три месяца (от переданной даты)."""
    # time_now = datetime.datetime.now()
    time_now = datetime.datetime.strptime("2021-12-31 23:00:01", "%Y-%m-%d %H:%M:%S")
    if date is None:
        date_ex2 = time_now
        date_ex1 = date_ex2 - relativedelta(months=3)
    else:
        date_ex2 = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        date_ex1 = date_ex2 - relativedelta(months=3)
    filtered_df: pd.DataFrame
    filtered_df = transactions_df[
        ((transactions_df["Категория"] == category) |
         (transactions_df["Описание"] == category))
        ]
    # отсортировать по дате
    # (transactions_df["Дата операции"] >= date_ex1) &
    # (transactions_df["Дата операции"] <= date_ex2) &
    return filtered_df

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_name = ROOT_DIR + "\\data\\operations1.xlsx"
data_list = read_trans_excel(file_name)
df1 = pd.DataFrame(data_list)

print("filt\n",spending_by_category(df1, "Связь","2021-12-31 23:00:01"))


# pip install python-dateutil