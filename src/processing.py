from datetime import datetime
from typing import Dict, List
from collections import Counter

import re


def sort_by_date(data_list: List[dict], reverse1: bool = True) -> List[dict]:
    """Функия принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание). Функция
    должна возвращать новый список, отсортированный по дате (date)"""
    # Преобразуем строки дат в объекты datetime для корректной сортировки
    list_sorted = sorted(
        data_list, key=lambda x: datetime.fromisoformat(x["date"].replace("Z", "+00:00")), reverse=reverse1
    )
    return list_sorted


def filter_by_state(banking_operations: List[Dict[str, str]], state: str = "EXECUTED") -> List[dict]:
    filtered_list: List[dict] = []
    # функция фильтрует данные по статусу
    for dict_item in banking_operations:
        if dict_item.get("state") == state:
            filtered_list.append(dict_item)
    return filtered_list


def process_bank_search(list_dict: list[dict], search_string: str) -> list[dict]:
    """принимает список словарей с данными о банковских операциях и строку поиска, а возвращает список словарей,
    у которых в описании есть данная строка."""
    try:
        new_list_dict = list()

        pattern = re.compile(search_string, re.IGNORECASE)
        for item in list_dict:
            key_value = item.get("description")
            if key_value and pattern.search(key_value):
                new_list_dict.append(item)

    except Exception as e:
        print(f"Внимание! Ошибка {e}! Введены не корректные данные!")

    return new_list_dict


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """принимает список словарей с данными о банковских операциях и список категорий операций, а возвращает словарь,
    в котором ключи — это названия категорий, а значения — это количество операций в каждой категории."""
    categories_counter = Counter()
    for operation in data:
        description = operation.get("description", "")
        for category in categories:
            if category.lower() in description.lower():
                categories_counter[category] += 1
    return categories_counter