#  coding=utf-8

from impalasqlHelper import *
from models import *
import uuid
import json


def get_manage_user(table):
    helper = ImpalasqlHelper()
    res = helper.get_all(table.user_id, table.user_name, table.password,
                         table.project, table.role_id, table.email, table=table.table)
    helper.close_impala()
    return res


def update_manage_user(data):
    helper = ImpalasqlHelper()
    for i in data:
        # 避免插入主键
        user_id = i.pop(manage_user.user_id)
        helper.update(manage_user.table, i, {manage_user.user_id: user_id})
    helper.close_impala()


def add_manage_user(data):
    helper = ImpalasqlHelper()
    helper.add(manage_user.table, data, {manage_user.user_id: str(uuid.uuid4())})
    helper.close_impala()


def get_manage_display(table):
    helper = ImpalasqlHelper()
    res = helper.get_all(table.display_id, table.display_name, table.display_name_chs,
                         table.project, table.category, table.icon, table=table.table)
    helper.close_impala()
    return res


def get_display(table):
    helper = ImpalasqlHelper()
    res = helper.get_all(table.display_id, table.display_name_chs, table.category, table=table.table)
    helper.close_impala()
    return translate(res)


def update_manage_display(data):
    helper = ImpalasqlHelper()
    for i in data:
        # 避免插入主键
        display_id = i.pop(manage_display.display_id)
        helper.update(manage_display.table, i, {manage_display.display_id: display_id})
    helper.close_impala()


def add_manage_display(data):
    helper = ImpalasqlHelper()
    helper.add(manage_display.table, data, {})
    helper.close_impala()


def get_manage_role(table):
    helper = ImpalasqlHelper()
    data = helper.get_all("distinct("+table.role_id+")", table.role_name, table.isdelete, table=table.table)
    res=[]
    for i in data:
        i["role_id"] = i.pop("distinct(role_id)")
        res.append(i)
    helper.close_impala()
    return res


def get_manage_role_by_id(role_id):
    helper = ImpalasqlHelper()
    res = helper.find(manage_role.table, {manage_role.role_id: role_id}, manage_role.role_id,
                      manage_role.display_id, manage_role.display_rename_chs, manage_role.isdisplay, manage_role.isdelete,
                      manage_role.role_name, manage_role.project)
    return res


def update_manage_role(data):
    helper = ImpalasqlHelper()

    role_id = data.pop(manage_role.role_id)
    helper.update(manage_role.table, data, {manage_role.role_id: role_id})
    helper.close_impala()


def add_manage_role(data, role_name):
    helper = ImpalasqlHelper()
    role_id = str(uuid.uuid4())
    for i in data:
        child = i.pop("child")

        print child
        for c in child:
            create_role(manage_role.table, get_data(c, role_name), {manage_role.role_id: role_id})
        create_role(manage_role.table, get_data(i, role_name), {manage_role.role_id: role_id})
    helper.close_impala()


def get_data(data, role_name):
    if isinstance(data, unicode):
        data = json.loads(data)
    res = {}
    res["display_id"] = data.get("display_id")
    res["role_name"] = role_name
    res["isdisplay"] = data.get("isdisplay")
    res["isdelete"] = "0"
    res["display_rename_chs"] = data.get("display_name_chs")
    return res


def create_role(table, data, rowkey):
    helper = ImpalasqlHelper()
    helper.add(table, data, rowkey)
    helper.close_impala()


def get_user_by_id(user_id):
    helper = ImpalasqlHelper()
    res = helper.find(manage_user.table, {manage_user.user_id: user_id}, manage_user.user_id, manage_user.role_id,
                manage_user.project, manage_user.email, manage_user.user_name)
    helper.close_impala()
    return res


def get_display_by_id(display_id):
    helper = ImpalasqlHelper()
    res = helper.find(manage_display.table, {manage_display.display_id: display_id}, manage_display.category,
                     manage_display.display_name, manage_display.display_name_chs, manage_display.icon,
                     manage_display.display_id)
    helper.close_impala()
    return res


def get_role_by_id(role_id):
    helper = ImpalasqlHelper()
    res = helper.find(manage_role.table, {manage_role.role_id: role_id}, manage_role.role_name, manage_role.isdelete,
                      manage_role.role_id, manage_role.display_rename_chs)
    helper.close_impala()
    if res:
        return [res[0]]
    return []




def translate(data):
    if data:
        father = []
        child = []
        for i in data:
            i["isdisplay"] = ""
            if i.get("display_id") == i.get("category"):
                father.append(i)
            child.append(i)

        res = []
        for f in father:
            fc = []
            for c in child:
                if f.get("category") == c.get("category"):
                    fc.append(json.dumps(c, ensure_ascii=False))
            f["child"] = fc
            res.append(f)
        return res

