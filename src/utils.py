import json
import logging
import os

# Получение корневого логера
root_logger = logging.getLogger()

ROOT_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


transaction_dict: dict = []
file_log = f"{ROOT_DIR}\\Logs\\util.log"
print(file_log)
fileExists = os.path.isfile(file_log)
if fileExists:
    os.remove(file_log)
# Создание и получение именованного логера
app_logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(file_log)
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
file_handler.setFormatter(file_formatter)
app_logger.addHandler(file_handler)
app_logger.setLevel(logging.DEBUG)
app_logger.debug('Debug message')


def read_json(filename=None) -> dict:
    """чтение файла json"""
    try:
        if os.path.isfile(filename):
            # Открываем файл и читаем строки
            with open(filename, encoding='utf-8') as f:
                json_list = json.load(f)
                if type(json_list) is list:
                    app_logger.info(" Удачный запуск")
                    return json_list
                else:
                    app_logger.error("Не удачный запуск")
                    return []
    except FileNotFoundError:
        # print("Файл не найден")
        app_logger.error("Файл не найден")
    except json.JSONDecodeError as e:
        # print(f"Сообщение об ошибке: {e.msg} Строка: {e.lineno}, колонка: {e.colno}")
        app_logger.error(f"Сообщение об ошибке: {e.msg} Строка: {e.lineno}, колонка: {e.colno}")
    except Exception as e:
        # print(e)
        app_logger.error(e)
