from src.item import Item


class Phone(Item):
    """
    класс для представления телефонов в магазине
    """
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        """
        метод для доступа к значению number_of_sim только для чтения
        """
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        """
        метод для генерации исключения в случае ошибочного изменения количества сим-карт и
        установки нового, если оно соответствует условиям
        """
        if not isinstance(value, int) or value <= 0:
            return ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        else:
            self._number_of_sim = value

    def __repr__(self):
        """
        метод для строкового представления объекта
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
