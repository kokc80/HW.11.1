from src.masks import get_mask_card_number


def get_date(date1: str) -> str:
    """
    Функция принимает на вход
    "2024 - 03 - 11    T02: 26:18.671407"
    и выдает дату в формате ДД.ММ.ГГГГ
    """
    temp_date: str
    temp_date = date1[: date1.find("T")]
    # применяю для того чтоб mypy не ругался на несоответствие типов
    date_2: list
    date_2 = temp_date.split("-")
    return f"{date_2[2].strip()}.{date_2[1].strip()}.{date_2[0].strip()}"


def mask_account_card(card_num: str) -> str:
    """
    Функция принимает на вход
    Visa Platinum 7000792289606361
    и выдает тип карты и номер карты
    """
    card_type: str = ""
    card_num_new: str = ""
    if card_num[:4] == "Счет":
        return f"Счет **{card_num[-4:]}"
    else:
        for i in range(len(card_num)):
            if card_num[i].isdigit() is True:
                card_num_new = card_num_new + card_num[i]
            else:
                card_type = card_type + card_num[i]
        card_num_new = get_mask_card_number(card_num_new)
        card_num_new = card_num_new.strip()
        return f"{card_type}  {card_num_new}"
