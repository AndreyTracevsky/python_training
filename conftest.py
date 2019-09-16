'''В ЭТОМ ФАЙЛЕ НАХОДИТСЯ ФИКСТУРА. @pytest.fixture(scope = "session") - ОТВЕЧАЕТ ЗА ЗАПУСК ТЕСТОВ В ЕДИНОЙ СЕССИИ БРАУЗЕРА (БРАУЗЕР ОТКРЫВАЕТСЯ 1 РАЗ И В НЕМ ЗАПУСКАЮТСЯ ВСЕ ИМЕЮЩИЕСЯ ТЕСТЫ).'''

import pytest
from fixture.application import Application


@pytest.fixture(scope = "session") # пометка для pytest, чтобы он знал что это не просто функция, а ф-ция создающая фикструру.
def app(request): # функция которая будет инициализироать фикстуру
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture