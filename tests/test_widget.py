import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "account_card, expected",
    [
        ("Счет 40817810240103456245", "Счет **6245"),
        ("Visa Classic 4256234567819034", "Visa Classic 4256 23** **** 9034"),
        ("Visa Gold 4276456122983471", "Visa Gold 4276 45** **** 3471"),
        ("Visa Platinum 4589678245671234", "Visa Platinum 4589 67** **** 1234"),
        ("MasterCard 7568223568902764", "MasterCard 7568 22** **** 2764"),
        ("Maestro 3300213475860990", "Maestro 3300 21** **** 0990"),
        ("МИР 2202202467890987", "МИР 2202 20** **** 0987"),
    ],
)
def test_mask_account_card(account_card, expected):
    assert mask_account_card(account_card) == expected


def test_get_date(input_date):
    assert get_date("2024-03-11T02:26:18.671407") == input_date
