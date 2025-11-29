import re
import os
from src.transaction_reader import read_trans_excel

def simple_search(data: list[dict], search_str: str) -> str:
    """Простой поиск
    Пользователь передает строку для поиска, возвращается JSON - ответ со всеми транзакциями, содержащими 
    запрос в описании или категории."""
    list_find = list()
    for item in data:
        value_1 = str(item.get("Описание", ""))
        value_2 = str(item.get("Категория", ""))
        if (search_str in value_1):
            list_find.append(item)
        if (search_str in value_2):
            list_find.append(item)
    return  list_find


