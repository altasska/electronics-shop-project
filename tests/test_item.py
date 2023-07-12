"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
from src.phone import Phone


def test_total_calculate():
    """
    Тест для проверки работоспособности метода, подсчитывающего общую стоимость конкретного товара.
    """
    item = Item("Смартфон", 10000, 10)
    total_calculate = item.calculate_total_price()

    assert total_calculate == 100000


def test_discount():
    """
    тест для правильности расчета установленной скидки для конкретного товара
    """
    item = Item("Смартфон", 10000, 10)
    Item.pay_rate = 0.85  # скидка 15%
    Item.apply_discount(item)

    assert item.price == 8500


def test_string_to_number():
    """
    тест для корректного преобразования строки в число, используя только целую часть
    """
    assert Item.string_to_number('5.6') == 5


def test_instantiate_from_csv():
    """
    тест для проверки корректности работы с cvs-файлом
    """
    Item.instantiate_from_csv()
    assert len(Item.all) == 5

    item1 = Item.all[0]
    assert item1.name == "Смартфон"
    assert item1.price == 100
    assert item1.quantity == 1


def test_name_setter():
    """
    тест для проверки корректности работы сеттера name
    """
    item = Item("Телефон", 10000, 5)

    item.name = "Смартфон"
    assert item.name == "Смартфон"

    item.name = "СуперСмартфонНаВсеВека"
    assert item.name == "СуперСмарт"


def test_repr():
    item = Item("Телефон", 10000, 5)
    assert repr(item) == "Item('Телефон', 10000, 5)"


def test_str():
    item = Item("Телефон", 10000, 5)
    assert str(item) == 'Телефон'


def test_phone_and_item_adding():
    item = Item("Смартфон", 10000, 20)
    phone = Phone("iPhone 14", 120_000, 5, 2)
    assert item + phone == 25
