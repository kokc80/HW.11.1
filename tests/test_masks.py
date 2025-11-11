import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    assert get_mask_card_number("7000792218960636") == "7000 79** **** 0636"
    assert get_mask_card_number("700289606361") == "7002 89** 6361"
    assert get_mask_card_number("") == ""


@pytest.mark.parametrize("card,expected", [("Счет 73654108430135874305", "**4305"), ("700289606361", "**6361")])
def test_get_mask_account(card, expected):
    assert get_mask_account(card) == expected


def test_get_mask_account_1():
    assert get_mask_account("Счет 73654108430135874305") == "**4305"
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("0") == "**0"
    assert get_mask_account("1") == "**1"
    assert get_mask_account("**") == "****"
    assert get_mask_account("") == ""
