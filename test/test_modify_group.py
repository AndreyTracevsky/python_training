from model.group import Group
# ТЕСТОВЫЕ МЕТОДЫ

def test_modify_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="Well DONE"))
    app.session.loguot()

def test_modify_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(header="Not bad"))
    app.session.loguot()

def test_modify_group_footer(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(footer="Very well"))
    app.session.loguot()