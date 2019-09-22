#  фУНКЦИЯ LOGIN И LOGOUT ПЕРЕМЕЩЕНЫ ИЗ ТЕСТОВЫХ МЕТОДОВ В РАЗНЫЕ ФИКСТУРЫ .
import pytest
from fixture.application import Application

fixture = None  # ГЛОБАЛЬНАЯ ПЕРЕМЕННАЯ


@pytest.fixture  # эта фикстура отвечает за авторизацию
def app(request):

    global fixture

    if fixture is None:
        fixture = Application()

    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture

# В этой фикстуре запуск тетстов проходит в одной сессии браузера
@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture