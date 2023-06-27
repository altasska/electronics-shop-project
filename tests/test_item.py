"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_total_calculate():
    """
    тест для проверки работоспособности метода, подсчитывающего общую стоимость конкретного товара
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
