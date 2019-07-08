from selenium.webdriver.firefox.webdriver import WebDriver # импорт перенесен сюда из файла test_add_group.py, т.к драйвер теперь будет запускаться
from fixture.session import SessionHelper
from fixture.group import GroupHelper

                               # тут.
class Application: # В этот класс перенесены все вспомогательные методы из файла test_add_group.py

    def __init__(self): # конструктор инициализации
        self.wd = WebDriver() # инициализация перенесенная из файла test_add_group.py
        self.wd.implicitly_wait(60)   #
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
 

    def open_home_page(self): # вспомогательный метод
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self): # Вспомогательный метод который останавливает драйвер (разрушает фикстуру)
        self.wd.quit()