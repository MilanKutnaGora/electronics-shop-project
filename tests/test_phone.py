from src.phone import Phone


def test_repr():
    """ Тестирование метода __repr__"""
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_Phone():
    """Тестирование поля кол-ва сим карт класса Phone"""
    phone = Phone("Смартфон", 50000, 10, 2)
    assert phone.number_of_sim == 2


def test_str():
    """ Тестирование метода __str__"""
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'


def test_setter():
    """Тестирование сеттера"""
    phone = Phone("Смартфон", 20000, 10, 5)
    phone.number_of_sim = 2
    assert phone.number_of_sim == 2
    phone.number_of_sim = 0
    assert phone.number_of_sim == 2