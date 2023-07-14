from src.keyboard import Keyboard
import pytest


@pytest.fixture
def keyboard():
    """
    фикстура для создания объекта класса Keyboard для простоты последующего
    использования в тестах
    """
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_keyboard_information(keyboard):
    assert keyboard.name == "Dark Project KD87A"
    assert keyboard.price == 9600
    assert keyboard.quantity == 5


def test_default_language(keyboard):
    assert keyboard.language == "EN"


def test_change_lang(keyboard):
    keyboard.change_lang()
    assert keyboard.language == "RU"
    keyboard.change_lang()
    assert keyboard.language == "EN"
    keyboard.change_lang()
    assert keyboard.language == "RU"


def test_invalid_language(keyboard):
    keyboard.language = "CH"
    assert AttributeError