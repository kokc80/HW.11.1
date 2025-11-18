from datetime import datetime
from typing import Dict, List
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


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """принимает список словарей с данными о банковских операциях и строку поиска, а возвращает список словарей,
    у которых в описании есть данная строка."""
    find_operations = []
    for operation in data:
        if re.search(search, operation.get('description', ''), flags = re.IGNORECASE):
            find_operations.append(operation)
    return find_operations


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """принимает список словарей с данными о банковских операциях и список категорий операций, а возвращает словарь,
    в котором ключи — это названия категорий, а значения — это количество операций в каждой категории."""
    pass