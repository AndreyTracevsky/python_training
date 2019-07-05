import pytest # переход на использование фрэймворка pytest
from model.group import Group # импортируем из файла group.py класс Group
from fixture.application import Application # импортируем из файла application.py класс Application


@pytest.fixture() # пометка для pytest, чтобы он знал что это не просто функция, а ф-ция создающая фикструру.
def app(request): # функция которая будет инициализироать фикстуру
    fixture = Application() # Создание самой фикстуры (объект типа Application)
    request.addfinalizer(fixture.destroy) #  передается функция которая в определенный момент передается для разрушения фикстуры
    return fixture # Возврат фикстуры

def test_add_group(app): # тестовый метод
    #wd = self.wd - Эта строка кода вырезается и вставляется в каждый из вспомогательных методов.
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="test", header="test", footer="test"))
    app.session.loguot()

def test_add_empty_group(app): # 2-й тестовый метод
    #wd = self.wd - Эта строка кода вырезается и вставляется в каждый из вспомогательных методов.
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.session.loguot()