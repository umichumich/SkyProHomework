import pytest
from src.generators import filter_by_currency

def test_filter_by_currency_exceptions(transactions):
    result = filter_by_currency(transactions, "EUR")
    assert list(result) == []
    result = filter_by_currency([], "EUR")
    assert result == "Список пустой!"