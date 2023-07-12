"""Здесь надо написать тесты с использованием pytest для модуля phone."""
import pytest

from src.phone import Phone
from src.item import Item


@pytest.fixture
def phone():
    """
    фикстура для создания объекта класса Phone для простоты последующего
    использования в тестах
    """
    return Phone("iPhone 14", 120_000, 5, 2)


@pytest.fixture
def item():
    """
    фикстура для создания объекта класса Item для простоты последующего
    использования в тестах
    """
    return Item("Смартфон", 10000, 20)


def test_phone_nformation(phone):
    assert phone.name == "iPhone 14"
    assert phone.price == 120000
    assert phone.quantity == 5
    assert phone.number_of_sim == 2


def test_phone_repr_information(phone):
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_phone_and_item_adding(phone, item):
    assert item + phone == 25


def test_phone_number_of_sim_setter_invalid_value():
    phone1 = Phone("iPhone 14", 120_000, 5, 0)
    assert ValueError
