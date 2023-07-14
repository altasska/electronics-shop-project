from src.item import Item


class LanguageMixin:
    """
    миксин для хранения/изменения языка на клавитуре
    """
    LANGUAGES = ["RU", "EN"]

    def __init__(self):
        self._language = "EN"

    @property
    def language(self):
        """
        метод для доступа к значению language только для чтения
        """
        return self._language

    @language.setter
    def language(self, value):
        """
        метод для генерации ошибки в случае неверного языка и установки верного,
        если он соответствует одному из заданных значений
        """
        if value in self.LANGUAGES:
            self._language = value
        else:
            return AttributeError

    def change_lang(self):
        """
        метод для смены раскладки
        """
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = "EN"


class Keyboard(Item, LanguageMixin):
    """
    класс, наследующий от Item и миксина
    """
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self._language = 'EN'

    def change_lang(self):
        super().change_lang()
        return self
