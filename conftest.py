'''фУНКЦИЯ LOGIN И LOGOUT ПЕРЕМЕЩЕНЫ ИЗ ТЕСТОВЫХ МЕТОДОВ В РАЗНЫЕ ФИКСТУРЫ .'''
import pytest
from fixture.application import Application

fixture = None # ГЛОБАЛЬНАЯ ПЕРЕМЕННАЯ

@pytest.fixture
def app(request): # функция которая будет инициализироать фикстуру
    global fixture # ОБЪЯВЛЕНИЕ ПЕРЕМЕННОЙ
    if fixture is None: # ПРОВЕРКА: "ЕСЛИ FIXTURE IS NONE, ТО ФИКСТУРУ НЕОБХОДИМО ПРОИНИЦИАЛИЗИРОВАТЬ, ЗАТЕМ ВЫПОЛНИТЬ ЛОГИН"
        fixture = Application()
        fixture.session.login(username="admin", password="secret") # ВЫПОЛНЕНИЕ ЛОГИНА
    else: # ПРОВЕРКА: "ЕСЛИ ФИКСТУРА СТАЛА НЕВАЛИДНОЙ, ТО ФИКСТУРУ НЕОБХОДИМО ПРОИНИЦИАЛИЗИРОВАТЬ, ЗАТЕМ ВЫПОЛНИТЬ ЛОГИН"
        if not fixture.is_valid(): # МЕТОД fixture.is_valid СОЗДАН В ФАЙЛЕ application.py
            fixture = Application()
            fixture.session.login(username="admin", password="secret")
    return fixture

'''В ДАННОЙ ФИКСТУРЕ ЧТОБЫ НЕ СОЗДАВАТЬ 2-А finalizer, ПЕРЕДЕЛАН СУЩЕСТВУЮЩИЙ КОТОРЫЙ БУДЕТ ВЫПОЛНЯТЬ СРАЗУ ДВА 
ДЕЙСТВИЯ(logout и destroy), РАНЬШЕ ВЫПЛНЯЛСЯ ТОЛЬКО DESTROY.'''
@pytest.fixture(scope="session", autouse=True) # scope="session" - запуск тестов в одной сессии браузера; autouse=True - выполняет фикстуру автоматически, даже если она нигде не указана.
def stop(request):
    def fin():
        fixture.session.loguot() # ВЫПОЛНЕНИЕ LOGOUT
        fixture.destroy() # ВЫПОЛНЕНИЕ DESTROY
    request.addfinalizer(fin)
    return fixture