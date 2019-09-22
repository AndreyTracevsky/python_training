from model.group import Group
# ТЕСТОВЫЕ МЕТОДЫ.

def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="Well DONE"))

def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="Not bad"))

def test_modify_group_footer(app):
    app.group.modify_first_group(Group(footer="Very well"))
