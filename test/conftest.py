import pytest # переход на использование фрэймворка pytest
from fixture.application import Application # импортируем из файла application.py класс Application


@pytest.fixture # пометка для pytest, чтобы он знал что это не просто функция, а ф-ция создающая фикструру.
def app(request): # функция которая будет инициализироать фикстуру
    fixture = Application() # Создание самой фикстуры (объект типа Application)
    request.addfinalizer(fixture.destroy) #  передается функция которая в определенный момент передается для разрушения фикстуры
    return fixture # Возврат фикстуры