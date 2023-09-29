"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item

def test___repr__():
    """
    Тестирование функции __repr__.

    """
    item1 = Item("Смартфон", 10000, 20)
    result = item1.__repr__()
    assert result == "Смартфон"


def test_string_to_number():
    """
        Тестирование функции string_to_number.

        """

    assert Item.string_to_number('1') == 1
    assert Item.string_to_number('2.0') == 1
    assert Item.string_to_number('2.2') == 1