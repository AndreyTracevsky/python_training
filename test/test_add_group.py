from model.group import Group # импортируем вспомогательные методы для запуска тестов

# ТЕСТОВЫЕ МЕТОДЫ
def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="test", header="test", footer="test"))
    app.session.loguot()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.loguot()