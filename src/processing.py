from typing import Dict, List
from datetime import datetime
from typing import List

def filter_by_state(banking_operations: List[Dict[str, str]], state: str = "EXECUTED") -> List:
    filtered_list: List = []
    for dict_item in banking_operations:
        if dict_item.get("state") == state:
            filtered_list.append(dict_item)
    return filtered_list


def sort_by_date(data_list: List[dict], reverse1: bool = True) -> List[dict]:
    """Функия принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание). Функция
    должна возвращать новый список, отсортированный по дате (date)"""
    # Преобразуем строки дат в объекты datetime для корректной сортировки
    list_sorted = sorted(
        data_list,
        key=lambda x: datetime.fromisoformat(x["date"].replace('T', '+00:00')),
        reverse=reverse1
    )
    return list_sorted


