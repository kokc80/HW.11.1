import os, json


def read_json(filename=None) -> dict:
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
    except FileNotFoundError:
        print("Файл не найден")
        return []
    except json.JSONDecodeError as e:
        print("Ошибка декодирования JSON!")
        print(f"Сообщение об ошибке: {e.msg}")
        print(f"Строка: {e.lineno}, колонка: {e.colno}")
    except Exception as e:
        print(e)