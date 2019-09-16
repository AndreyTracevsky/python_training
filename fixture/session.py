
class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password): # вспомогательный метод
        wd = self.app.wd
        self.app.open_home_page() # перенесен сюда из метода "def test_add_group(self)" (аналогично проделано для каждого) вспомогательного метода
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def loguot(self):  # вспомогательный метод
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("user")