import csv
import os

GOOD_PATH = os.path.join(os.path.dirname(__file__), 'items.csv')
ABSOLUTE_PATH = os.path.abspath(GOOD_PATH)


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self._name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if len(value) <= 10:
            self._name = value
        else:
            self._name = value[:10]

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
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """
        Метод для создания объектов класса Item на основе соответствующего csv-файла.
        """
        cls.all = []  # очистка списка объектов перед созданием новых объектов из файла
        with open(ABSOLUTE_PATH, 'r', newline='') as file:  # У
            r = csv.DictReader(file)
            for line in r:
                name = line['name']
                price = float(line['price'])
                quantity = int(line['quantity'])
                item = cls(name, price, quantity)

    @staticmethod
    def string_to_number(value: str) -> int:
        s = float(value)
        return int(s)
