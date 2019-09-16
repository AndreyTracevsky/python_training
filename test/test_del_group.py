

def test_delete_first_group(app): # тестовый метод
    app.session.login(username="admin", password="secret")
    app.group.delete_first_group()
    app.session.loguot()
