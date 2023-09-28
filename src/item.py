import csv

import pytest


class Item:
    """
    Класс для представления товара в магазине.
    """
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"


    def __str__(self):
        return f"{self.name}"


if __name__ == '__main__':
    item1 = Item("Смартфон", 10000, 20)

    print(repr(item1))
    print(item1)

pytest.main()





