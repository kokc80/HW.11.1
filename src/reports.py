import datetime
import pandas as pd
import os
import json
from src.transaction_reader import read_trans_excel
from dateutil.relativedelta import relativedelta


def spending_by_category(df: pd.DataFrame, category: str, date: str | None = None) -> pd.DataFrame:
    """Функция возвращает траты по заданной категории за последние три месяца (от переданной даты)."""
    # time_now = datetime.datetime.now()
    time_now = datetime.datetime.strptime("2021-12-31 23:00:01", "%Y-%m-%d %H:%M:%S")
    if date is None:
        date_ex2 = time_now
        date_ex1 = date_ex2 - relativedelta(months=3)
    else:
        date_ex2 = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        date_ex1 = date_ex2 - relativedelta(months=3)
    # отсортировать по дате
    df["Дата операции"] = pd.to_datetime(df["Дата операции"], dayfirst=True)
    filtered_df = df[((df['Дата операции'] >= date_ex1) & (df['Дата операции'] <= date_ex2))]
#    print("filtr\n",filtered_df)
#    (df["Категория"] == category | df["Описание"] == category)]
    #    sorted_df = filtered_df.sort_values(by='Дата операции', ascending=True)
    temp_df = filtered_df
#    print("filtered date\n",temp_df)
    filtered_df = temp_df[(temp_df["Категория"] == category) | (temp_df["Описание"] == category)]
#    print("filtered\n",filtered_df)
    return filtered_df

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_name = ROOT_DIR + "\\data\\operations1.xlsx"
data_list = read_trans_excel(file_name)

df1 = pd.DataFrame(data_list)
df1["Дата операции"] = pd.to_datetime(df1["Дата операции"], dayfirst=True)

simplesearch_out = spending_by_category(df1, "Связь","2018-01-30 23:00:01")
# out_list = simplesearch_out.to_dict("records")
print("filtered\n",simplesearch_out)



# json_out = json.dumps(out_list, ensure_ascii=False, indent=2)
# print(json_out)

# pip install python-dateutil