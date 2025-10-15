def get_mask_card_number(card_num: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску.
    Номер карты замаскирован и отображается в формате, где X — это цифра
    номера. То есть видны первые 6 цифр и последние 4 цифры, остальные
    символы отображаются звездочками, номер разбит по блокам по 4 цифры,
    разделенным пробелами.
    Пример работы функции:
    get_mask_card_number
    XXXX XX** **** XXXX
    7000792289606361 # входной аргумент
    7000 79** **** 6361 # выход функции
    """
    new_card_num: str = ""
    for i in range(len(card_num)):
        if i >= 0 and i <= 5:
            new_card_num = new_card_num + card_num[i]
        elif i >= 6 and i <= len(card_num) - 5:
            new_card_num = new_card_num + "*"
        elif i > len(card_num) - 5 and i <= len(card_num):
            new_card_num = new_card_num + card_num[i]
        if (i + 1) % 4 == 0:
            new_card_num = new_card_num + " "
    new_card_num = new_card_num.strip()
    return new_card_num


def get_mask_account(invoice_num: str) -> str:
    """
    Функция get_mask_account принимает на вход номер счета и возвращает его
    маску. Номер счета замаскирован и отображается в формате **XXXX, где
    X — это цифра номера.
    То есть видны только последние 4 цифры номера, а перед ними —
    две звездочки.
    Пример работы функции:
    73654108430135874305  # входной аргумент
    **4305  # выход функции
    """
    new_invoice_num: str = ""
    if invoice_num == "":
        new_invoice_num = ""
    else:
        new_invoice_num = "**" + invoice_num[-4:]
    return new_invoice_num.strip()
