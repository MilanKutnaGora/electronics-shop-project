import csv


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
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        """Магический метод для отображения информации об объекте класса в режиме отладки"""
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """Магический метод для отображения информации об объекте класса для пользователей"""
        return f"{self.__name}"


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):

        value = value[:10]
        self.__name = value

    @classmethod
    def instantiate_from_csv(cls, path):
        cls.all.clear()
        input_file = csv.DictReader(open(path, encoding="utf-8"))
        for itemdata in input_file:
            cls(itemdata['name'], itemdata['price'], itemdata['quantity'])

    @staticmethod
    def string_to_number(string_num):
        """Статический метод, возвращающий число из числа-строки"""
        return int(float(string_num))









