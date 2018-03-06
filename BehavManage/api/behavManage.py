#  coding:utf-8

from manage import app
from flask import request, redirect, render_template
from config import *
from result import *
from service import behavManageService, models
from flask import json


@app.route('/login', methods=['POST'])
def login():
    if request.form.get('username') == name:
        if request.form.get('password') == password:
            return Succeed('登陆成功')

        return Fail("密码错误")
    else:
        return Fail("用户名错误")


@app.route('/manage_user',  methods=['POST', 'GET', 'PUT', 'DELETE'])
def manage_user():

    if request.method == 'GET':
        return SucceedResult(behavManageService.get_manage_user(models.manage_user))
    if request.method == 'PUT':
        behavManageService.update_manage_user(json.loads(request.data).get("data"))
        return Succeed("更新成功")
    if request.method == 'POST':
        behavManageService.add_manage_user(json.loads(request.data).get("data"))
        return Succeed("添加成功")


@app.route('/get_user',  methods=['GET'])
def getUserById():
    if request.method == 'GET':
        user_id = request.args.get("user_id")
        return SucceedResult(behavManageService.get_user_by_id(user_id))


@app.route('/get_display',  methods=['GET'])
def getDisplayById():
    if request.method == 'GET':
        display_id = request.args.get("display_id")
        return SucceedResult(behavManageService.get_display_by_id(display_id))


@app.route('/get_role',  methods=['GET'])
def getRoleById():
    if request.method == 'GET':
        role_id = request.args.get("role_id")
        return SucceedResult(behavManageService.get_role_by_id(role_id))


@app.route('/manage_display',  methods=['POST', 'GET', 'PUT', 'DELETE'])
def manage_display():

    if request.method == 'GET':
        return SucceedResult(behavManageService.get_manage_display(models.manage_display))
    if request.method == 'PUT':
        behavManageService.update_manage_display(json.loads(request.data).get("data"))
        return Succeed("更新成功")
    if request.method == 'POST':
        behavManageService.add_manage_display(json.loads(request.data).get("data"))
        return Succeed("添加成功")


@app.route('/manage_role',  methods=['POST', 'GET', 'PUT', 'DELETE'])
def manage_role():

    if request.method == 'GET':
        return SucceedJsonResult(behavManageService.get_manage_role(models.manage_role))
    if request.method == 'PUT':
        behavManageService.update_manage_role(json.loads(request.data).get("data"))
        return Succeed("更新成功")
    if request.method == 'POST':
        behavManageService.add_manage_role(json.loads(request.data).get("data"),
                                           json.loads(request.data).get("role_name"))
        return Succeed("添加成功")


@app.route('/get_display',  methods=['GET'])
def get_display():
    if request.method == 'GET':
        return SucceedJsonResult(behavManageService.get_display(models.manage_display))
