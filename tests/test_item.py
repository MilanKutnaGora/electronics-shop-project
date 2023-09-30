"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest
def test_item_params():
    """Тестирование полей класса Item"""
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert item1.name == "Смартфон"
    assert item2.name == "Ноутбук"
    assert item1.price == 10000
    assert item2.price == 20000
    assert item1.quantity == 20
    assert item2.quantity == 5


def test_string_to_number():
    """Тестирование метода string_to_number"""
    assert Item.string_to_number('7') == 7
    assert Item.string_to_number('9.5') == 9
    assert Item.string_to_number('10.2') == 10

def test_name():
    """ Тестирование длины наименования товара"""
    item = Item('Телефон', 10000, 5)
    item.name = 'СуперСмартфон'

    assert len(item.name) == 10

def test_repr():
    """ Тестирование метода __repr__"""
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"

def test_str():
    """ Тестирование метода __str__"""
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'