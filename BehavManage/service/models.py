#  coding:utf-8


class manage_user:
    table = 'manage_user'
    user_id = 'user_id'
    user_name = 'user_name'
    password = 'password'
    project = 'project'
    role_id = 'role_id'
    email = 'email'


class manage_role:
    table = 'manage_role'
    role_id = 'role_id'
    display_id = 'display_id'
    role_name = 'role_name'
    isdisplay = 'isdisplay'
    isdelete = 'isdelete'
    project = 'project'
    display_rename_chs = 'display_rename_chs'


class manage_display:
    table = 'manage_display'
    display_id = 'display_id'
    display_name = 'display_name'
    display_name_chs = 'display_name_chs'
    project = 'project'
    category = 'category'
    icon = 'icon'


