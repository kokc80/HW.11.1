import datetime
import io
import os

import pandas as pd
from dateutil.relativedelta import relativedelta

from src.transaction_reader import read_trans_excel

def searching_date(d1: str | None = None):
    """Функция для перевода строки в datetime
    возвращает словарь из {даты начала} и {даты окончания} = {дата начала} - 3 месяца"""
    if d1 is None:
        date_ex2 = time_now
        date_ex1 = date_ex2 - relativedelta(months=3)
    else:
        date_ex2 = datetime.datetime.strptime(d1, "%Y-%m-%d %H:%M:%S")
        date_ex1 = date_ex2 - relativedelta(months=3)
    return {"Дата начала": date_ex1, "Дата окончания": date_ex2}


def spending_by_category(df: pd.DataFrame, category: str, date_f: str | None = None) -> pd.DataFrame:
    """Функция возвращает траты по заданной категории за последние три месяца (от переданной даты)."""
    # time_now = datetime.datetime.now()
    dates = searching_date(date_f)
    date_ex1 = dates["Дата начала"]
    date_ex2 = dates["Дата окончания"]
    # отсортировать по дате
    df["Дата операции"] = pd.to_datetime(df["Дата операции"], dayfirst=True)
    filtered_df = df[((df['Дата операции'] >= date_ex1) & (df['Дата операции'] <= date_ex2))]
    temp_df = filtered_df
    filtered_df = temp_df[(temp_df["Категория"] == category) | (temp_df["Описание"] == category)]
    filered_ld = filtered_df.to_json(force_ascii=False)
    df_out = pd.read_csv(io.StringIO(filered_ld))
    return (df_out)


ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


file_name = ROOT_DIR + "\\data\\operations1.xlsx"
data_list = read_trans_excel(file_name)

df1 = pd.DataFrame(data_list)
df1["Дата операции"] = pd.to_datetime(df1["Дата операции"], dayfirst=True)
print("datafr\n\n",spending_by_category(df1, "Связь", "2018-01-30 23:00:01"))
