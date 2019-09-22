'''В данном файле происходит инициализация Web Driver, а также открытие необходимой страницы в браузере.'''
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:

    def __init__(self): # конструктор инициализации
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def is_valid(self):
       try:
           self.wd.current_url # ЗАПРОС В БРАУЗЕР АДРЕС ОТКРЫТОЙ ТЕКУЩЕЙ СТРАНИЦЫ
           return True         # ЕСЛИ ВСЕ ХОРОШО, ТО ВОЗВРАЩАЕТСЯ ЗНАЧЕНИЕ TRUE
       except:
           return False        # ЕСЛИ ВСЕ ПЛОХО, ВОЗВРАЩАЕТС ЗНАЧЕНИЕ FALSE


    def open_home_page(self): # вспомогательный метод который открывает нужную страницу
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self): # Метод который останавливает драйвер (разрушает фикстуру)
        self.wd.quit()