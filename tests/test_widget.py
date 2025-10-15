from src.widget import *


def test_get_date():
    assert get_date("2024 - 03 - 11    T02: 26:18.671407") == "11.03.2024"


def test_mask_account_card():
    assert mask_account_card("") == "  "
    assert mask_account_card("Счет 7000792289606361") == "Счет **6361"
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum   7000 79** **** 6361"
