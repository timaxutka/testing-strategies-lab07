import pytest
from task1.solution import days_between_dates

@pytest.mark.parametrize("d1, d2, expected", [
    ("01.01.2020", "02.01.2020", 1),
    ("15.05.2021", "15.05.2021", 0),
    ("31.12.2020", "01.01.2021", 1),
    ("01.01.2023", "01.01.2022", 365),
    ("28.02.2020", "01.03.2020", 2)  # високосный год
])
def test_days_valid(d1, d2, expected):
    assert days_between_dates(d1, d2) == expected

def test_days_invalid():
    with pytest.raises(ValueError):
        days_between_dates("31-02-2020", "01.03.2020")
