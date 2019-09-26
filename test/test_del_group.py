# ТЕСТОВЫЙ МЕТОД.
from model.group import Group

def test_delete_first_group(app):
    if app.group.count() == 0:                           # предусловие которое проверяет наличие хотя бы "группы" на странице ->
        app.group.create(Group(name = "Creating group")) # -> если "группа" отсутсвует на странице, то выполняется создание группы.
    app.group.delete_first_group()                       # строка которая уадаляет первую в списке группу
