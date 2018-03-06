#  coding=utf-8

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from manage import *
from config import *


def run():
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(port=web_port, address="0.0.0.0")  # 对应flask的端口
    IOLoop.instance().start()


if __name__ == "__main__":
    run()
