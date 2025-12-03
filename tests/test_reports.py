import datetime
import pytest
from src.reports import searching_date

dt_s = "2018-01-30 23:00:01"
def test_searching_date():
    expected = {"Дата начала": datetime.datetime(2017, 10, 30, 23, 0, 1),
                "Дата окончания": datetime.datetime(2018, 1, 30, 23, 0, 1)}
    assert searching_date(dt_s) == expected
