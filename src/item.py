import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        # Item.all.append(self)

    def __repr__(self):
        """Магический метод для отображения информации об объекте класса в режиме отладки"""
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"


    def __str__(self):
        """Магический метод для отображения информации об объекте класса для пользователей"""
        return f"{self.__name}"


    @classmethod
    def instantiate_from_csv(cls, filename):
        """Класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv"""
        file_path = os.path.join(os.path.split(os.path.dirname(__file__))[0],
                                 *os.path.split(filename))
        print(file_path)
        with open(file_path, newline='', encoding='windows-1251') as csvfile:
            reader = csv.DictReader(csvfile)
            cls.all.clear()
            for row in reader:
                cls.all.append(cls(row["name"], row["price"], row["quantity"]))

    @staticmethod
    def string_to_number(string_num):
        """Статический метод, возвращающий число из числа-строки"""
        return int(float(string_num))


    @property
    def name(self):
        """Класс name getter"""
        return self.__name

    @name.setter
    def name(self, new_name):
        """Класс name setter"""
        self.__name = new_name[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate










