import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(list_state):
    assert filter_by_state(list_state) == list_state


def test_sort_by_date(sorted_inform_state):
    assert sort_by_date(sorted_inform_state) == sorted_inform_state
