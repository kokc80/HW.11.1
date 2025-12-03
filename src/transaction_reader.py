import csv
import logging
import os

import pandas as pd

root_logger = logging.getLogger()

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_log = f"{ROOT_DIR}\\Logs\\trans_read.log"
# очистка файла лога
with open(file_log, "w"):
    app_logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler(file_log)
    file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
    file_handler.setFormatter(file_formatter)
    app_logger.addHandler(file_handler)
    app_logger.setLevel(logging.DEBUG)
    app_logger.debug("Debug message")


def read_trans_csv(filename=None) -> list[dict]:
    # Функция считывания словаря транзакций из файла csv
    try:
        # print(filename)
        if os.path.isfile(filename):
            # Открываем файл и читаем строки
            with open(filename, encoding="utf-8") as trans_file:
                csv_reader = csv.DictReader(trans_file)
                app_logger.info(" Удачный запуск")
                return list(csv_reader)
        else:
            return list()
    except FileNotFoundError:
        app_logger.error("Файл не найден")
    except Exception as e:
        app_logger.error(e)


def read_trans_excel(filename=None) -> list[dict]:
    # функция для чтения из Excel файла
    try:
        if os.path.isfile(filename):
            # Открываем файл и читаем строки
            excel_reader = pd.read_excel(filename)
            app_logger.info(" Удачный запуск")
            excel_reader = excel_reader.fillna({})
            return excel_reader.to_dict("records")
        else:
            return []
    except FileNotFoundError:
        app_logger.error("Файл не найден")
    except Exception as e:
        app_logger.error(e)
