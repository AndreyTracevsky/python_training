from selenium import webdriver # импорт перенесен сюда из файла test_add_group.py, т.к драйвер теперь будет запускаться
                               # тут.
class Application: # В этот класс перенесены все вспомогательные методы из файла test_add_group.py

    def __init__(self): # конструктор инициализации
        self.wd = webdriver.Firefox() # инициализация перенесенная из файла test_add_group.py
        self.wd.implicitly_wait(30)   #

    def loguot(self): # вспомогательный метод
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self): # вспомогательный метод
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def create_group(self, group): # вспомогательный метод
        wd = self.wd
        self.open_groups_page() # перенесен сюда из метода "def test_add_group(self)"
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page() # перенесен сюда из метода "def test_add_group(self)"

    def open_groups_page(self): # вспомогательный метод
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def login(self, username, password): # вспомогательный метод
        wd = self.wd
        self.open_home_page() # перенесен сюда из метода "def test_add_group(self)" (аналогично проделано для каждого)
                              # вспомогательного метода
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self): # вспомогательный метод
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self): # Вспомогательный метод который останавливает драйвер (разрушает фикстуру)
        self.wd.quit()