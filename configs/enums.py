from enum import Enum


class GlobalErrorMessages(Enum):
    WRONG_TITLE = "Некорректный title страницы!"
    WRONG_URL = "Некорректные URL данные!"
    WRONG_TEXT = "Некорректный/неожидаемый текст!"
    WRONG_LIST = "Некорректный/неожидаемый список!"
    WRONG_ELEMENT = "Некорректный/ненайденный элемент!"
    WRONG_LINK = "Некорректная/ненайденная ссылка!"
    WRONG_COUNTER = "Некорректное количество элементов!"
    WRONG_LENGHT = "Длина списка некорректная!"
