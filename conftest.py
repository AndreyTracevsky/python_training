import pytest # переход на использование фрэймворка pytest
from fixture.application import Application # импортируем из файла application.py класс Application


@pytest.fixture(scope = "session") # пометка для pytest, чтобы он знал что это не просто функция, а ф-ция создающая фикструру.
def app(request): # функция которая будет инициализироать фикстуру
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture