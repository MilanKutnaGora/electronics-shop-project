from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        if number_of_sim >= 0:
            self.number_of_sim = number_of_sim


    def __repr__(self):
        """Магический метод для отображения информации об объекте класса в режиме отладки"""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"


    def __str__(self):
        """Магический метод для отображения информации об объекте класса для пользователей"""
        return f"{self.name}"


    @property
    def number_of_sim(self):
        """Геттер для количества сим-карт"""
        return self.__number_of_sim


    @number_of_sim.setter
    def number_of_sim(self, value):
        """Сеттер для количества сим-карт"""
        if value <= 0 or not isinstance(value, int):
            print(f"ValueError:Количество физических SIM-карт должно быть целым числом больше нуля.")
        self.__number_of_sim = value



