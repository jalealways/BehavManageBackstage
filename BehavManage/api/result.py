#  coding=utf-8

from flask import jsonify
import json

def Succeed(msg):
    return jsonify({"success": True, "message": msg})


def Fail(msg):
    return jsonify({"success": False, "message": msg})


def SucceedResult(msg):
    return jsonify({"success": True, "data": msg})


def SucceedJsonResult(msg):
    return json.dumps({"success": True, "data": msg}, ensure_ascii=False)

