from model.group import Group # импортируем из файла group.py класс Group


def test_add_group(app): # тестовый метод
    #wd = self.wd - Эта строка кода вырезается и вставляется в каждый из вспомогательных методов.
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="test", header="test", footer="test"))
    app.session.loguot()

def test_add_empty_group(app): # 2-й тестовый метод
    #wd = self.wd - Эта строка кода вырезается и вставляется в каждый из вспомогательных методов.
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.loguot()