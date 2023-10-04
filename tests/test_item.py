# """"Здесь надо написать тесты с использованием pytest для модуля item."""
# import pytest
# from src.item import Item, InstantiateCSVError
# from src.phone import Phone
#
# def test_item_params():
#     """Тестирование полей класса Item"""
#     item1 = Item("Смартфон", 10000, 20)
#     item2 = Item("Ноутбук", 20000, 5)
#
#     assert item1.name == "Смартфон"
#     assert item2.name == "Ноутбук"
#     assert item1.price == 10000
#     assert item2.price == 20000
#     assert item1.quantity == 20
#     assert item2.quantity == 5
#
#
# def test_item_calculate_total_price():
#     """Тестирование метода расчета количества товара"""
#     item1 = Item("Смартфон", 10000, 20)
#     item2 = Item("Ноутбук", 20000, 5)
#
#     assert item1.calculate_total_price() == 200000
#     assert item2.calculate_total_price() == 100000
#
#
# def test_apply_discount():
#     """Тестирование метода применения скидки возвращающий None"""
#     item1 = Item("Смартфон", 10000, 20)
#     item2 = Item("Ноутбук", 20000, 5)
#
#     Item.pay_rate = 0.8
#     item1.apply_discount()
#     item2.apply_discount()
#
#     assert item1.price == 8000
#     assert item2.price == 16000
#
#
# def test_instantiate_from_csv():
#     """Тестирование метода instantiate_from_csv"""
#     file_path = 'tests/test_items.csv'
#     Item.instantiate_from_csv(file_path)
#
#     assert len(Item.all) == 5
#
#
# def test_string_to_number():
#     """Тестирование метода string_to_number"""
#     assert Item.string_to_number('7') == 7
#     assert Item.string_to_number('9.5') == 9
#     assert Item.string_to_number('10.2') == 10
#
# def test_name():
#     """ Тестирование длины наименования товара"""
#     item = Item('Телефон', 10000, 5)
#     item.name = 'СуперСмартфон'
#
#     assert len(item.name) == 10
#
# def test_repr():
#     """ Тестирование метода __repr__"""
#     item1 = Item("Смартфон", 10000, 20)
#     assert repr(item1) == "Item('Смартфон', 10000, 20)"
#
# def test_str():
#     """ Тестирование метода __str__"""
#     item1 = Item("Смартфон", 10000, 20)
#     assert str(item1) == 'Смартфон'
#
#
# def test_empty_csv():
#     """Тестирование пустого файла"""
#     with pytest.raises(FileNotFoundError):
#         Item.instantiate_from_csv("item.csv")
#
#
# def test_broken_csv():
#     """Тестирование поврежденного файла"""
#     with pytest.raises(InstantiateCSVError):
#         Item.instantiate_from_csv("../src/item.csv")





import pytest
from src.item import Item, InstantiateCSVError
from src.phone import Phone


def test_Item():
    """Тестирование полей класса Item"""
    item1 = Item("Плазма", 200000, 2)
    assert item1.name == "Плазма"
    assert item1.price == 200000
    assert item1.quantity == 2
    item1.name = "Утюг"
    assert item1.name == "Утюг"
    item1.name = "Утюг крутой супер"
    assert item1.name == "Утюг круто"


def test_calculate_total_price():
    """Тестирование метода расчета количества товара"""
    item1 = Item("Смартфон", 5, 10)
    item2 = Item("Ноутбук", 2, 50000)
    assert item1.calculate_total_price() == 50
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    """Тестирование метода применения скидки возвращающий None"""
    item1 = Item("Наушники", 15000, 80)
    assert item1.apply_discount() is None


def test_Item_string_to_number():
    """Тестирование статик-метода"""
    assert Item.string_to_number("6") == 6
    assert Item.string_to_number("10.4") == 10


def test_repr():
    """Тестирование repr"""
    item = Item("Весы", 3000, 8)
    assert repr(item) == "Item('Весы', 3000, 8)"
    assert str(item) == 'Весы'


def test_add():
    """Тестирование add"""
    item = Item("Планшет", 10000, 50)
    phone = Phone("Смартфон", 30000, 30, 1)
    assert item + phone == 80
    assert phone + phone == 60
    assert item + 50 == "Нельзя складывать объекты разных классов"
    assert phone + 100 == "Нельзя складывать объекты разных классов"


def test_empty_csv():
    """Тестирование пустого файла"""
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv("item.csv")


def test_broken_csv():
    """Тестирование поврежденного файла"""
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv("../src/item.csv")