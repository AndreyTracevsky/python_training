from model.group import Group # импортируем вспомогательные методы для запуска тестов

# ТЕСТОВЫЕ МЕТОДЫ
def test_add_group(app):
    app.group.create(Group(name="test", header="test", footer="test"))

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
