

def test_add_group(app):
    group_name = 'test group form f'
    old_list = app.group.get_group_list()
    app.group.add_new_group(group_name)
    new_list = app.group.get_group_list()
    old_list.append(group_name)
    assert sorted(old_list) == sorted(new_list)
    app.main.exit()


