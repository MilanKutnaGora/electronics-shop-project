"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item

def test__repr__():
    """
    Тестирование функции __repr__.

    """
    item1 = Item("Смартфон", 10000, 20)
    result = item1.__repr__()
    assert result == "Item('Смартфон', 10000, 20)"

def test__str__():
    """
        Тестирование функции __str__.

    """
    item1 = Item("Смартфон", 10000, 20)
    result = item1.__str__()
    assert result == "Смартфон"


