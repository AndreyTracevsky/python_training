''' В этом файле находятся вспомогательные методы по:
- создание/удаление/МОДИФИКАЦИЯ (NAME, HEADER, FOOTER)  группы
- открытие goup_page
- возврат к group_page
'''

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self): # вспомогательный метод
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create(self, group): # вспомогательный метод
        wd = self.app.wd
        self.open_groups_page() # ССЫЛКА НА ВСПОМОГАТЕЛЬНЫЙ МЕТОД (НАХОДИТСЯ В ЭТОМ ФАЙЛЕ)
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def fill_group_form(self, group): # вспомогательный метод заполнения полей: name, header, footer
        wd = self.app.wd
        self.change_fill_value("group_name", group.name)
        self.change_fill_value("group_header", group.header)
        self.change_fill_value("group_footer", group.footer)

    def change_fill_value(self, field_name, text):
        wd = self.app.wd
        if text is not None: # ЕСЛИ ПАРАМЕТР text не = None, то выполняются действия которые описанны ниже
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        wd.find_element_by_name("update").click()

    def open_groups_page(self): # вспомогательный метод
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()