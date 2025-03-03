import csv
import os

GOOD_PATH = os.path.join(os.path.dirname(__file__), 'items.csv')
ABSOLUTE_PATH = os.path.abspath(GOOD_PATH)


class InstantiateCSVError(Exception):
    """
    класс для пользовательского исключения
    """

    def __init__(self, message="Файл item.csv поврежден"):
        self.message = message
        super().__init__(self.message)


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

    def __add__(self, other):
        """
        метод для сложения экземпляров класса
        (сложение по количеству товара в магазине)
        """
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            return None

    def __repr__(self):
        return f"{self.__class__.__name__}('{self._name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self._name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """
        сеттер для корректной обработки названия товара
        """
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

        try:

            with open(ABSOLUTE_PATH, 'r', newline='') as file:  # У
                r = csv.DictReader(file)
                for line in r:
                    if 'quantity' not in line:
                        raise InstantiateCSVError("Файл item.csv поврежден: отсутствует ключ 'quantity'")
                    name = line['name']
                    price = float(line['price'])
                    quantity = int(line['quantity'])
                    item = cls(name, price, quantity)

        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")

        except InstantiateCSVError:
            raise InstantiateCSVError()

    @staticmethod
    def string_to_number(value: str) -> int:
        """
        метод для преобразования строки в численное значение по целой части
        """
        s = float(value)
        return int(s)
