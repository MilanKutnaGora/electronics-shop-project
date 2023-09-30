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


def test_item_calculate_total_price():
    """Тестирование метода расчета количества товара"""
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    """Тестирование метода применения скидки возвращающий None"""
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    Item.pay_rate = 0.8
    item1.apply_discount()
    item2.apply_discount()

    assert item1.price == 8000
    assert item2.price == 16000


def test_instantiate_from_csv():
    """Тестирование метода instantiate_from_csv"""
    file_path = 'tests/test_items.csv'
    Item.instantiate_from_csv(file_path)

    assert len(Item.all) == 5


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