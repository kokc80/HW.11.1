import os, json


def read_json(filename=None) -> list:
    """чтение файла json"""
    try:
        if os.path.isfile(filename):
            # Открываем файл и читаем строки
            with open(filename, encoding='utf-8') as f:
                json_list = json.load(f)
                if type(json_list) is list:
                    return json_list
                else:
                    return []
    except:
        return[]