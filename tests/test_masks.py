import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("2202202456789045", "2202 20** **** 9045"),
        ("5649345789032013", "5649 34** **** 2013"),
        ("1111222233334444", "1111 22** **** 4444"),
    ],
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "acc_number, expected",
    [("40817810540107652134", "**2134"), ("40817810340101234567", "**4567"), ("40817810240107658902", "**8902")],
)
def test_get_mask_account(acc_number, expected):
    assert get_mask_account(acc_number) == expected
