import random


def test_delete_group(app):
    old_list = app.group.get_group_list()
    if len(old_list) <= 1:
        for i in range(2):
            app.group.add_new_group("Test group single %s" % i)
        old_list = app.group.get_group_list()
    group_to_delete = random.choice(old_list)
    app.group.delete_group(group_to_delete)
    new_list = app.group.get_group_list()
    old_list.remove(group_to_delete)
    assert sorted(old_list) == sorted(new_list)
    app.main.exit()
