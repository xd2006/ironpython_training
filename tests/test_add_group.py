

def test_add_group(app, xlsx_groups):
    group_name = xlsx_groups
    old_list = app.group.get_group_list()
    app.group.add_new_group(group_name)
    new_list = app.group.get_group_list()
    old_list.append(group_name)
    assert sorted(old_list) == sorted(new_list)


