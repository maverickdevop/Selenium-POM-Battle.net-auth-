import pytest

@pytest.mark.usefixtures('driver')
class BaseTest:
    """ Инициализация базового теста с фикстурой драйвера"""
    pass