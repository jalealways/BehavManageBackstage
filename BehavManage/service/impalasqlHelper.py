#  coding=utf-8

from config import *
from impala.dbapi import connect


class ImpalasqlHelper:

    def __init__(self):
        self.conn = connect(host=impala_host, port=impala_port, database=impala_database)
        self.cusor = self.conn.cursor()

    # def connect_impala(self):

    def close_impala(self):
        self.cusor.close()
        self.conn.close()

    def get_all(self, *args, **kwargs):
        # args为查询的字段， kwargs为table表名
        sql = 'select '+','.join(args)+' from '+kwargs['table']
        self.cusor.execute(sql)
        res = self.cusor.fetchall()
        nres = []
        if res:
            for i in res:
                dic = {}
                for j in range(0, len(args)):
                    dic[args[j]] = i[j]
                nres.append(dic)
        return nres

    def update(self, table, data, rowkey):
        # 更新操作 table为表名， data为是字典，是需要更新的内容， rowkey为字典，作为更新的条件，键为字段，将键值字符拼接
        da = ''
        for key, value in data.items():
            da += key.encode("utf-8")+"='"+value.encode("utf-8")+"',"

        wr = ''
        for k, v in rowkey.items():
            wr += k.encode("utf-8")+"='"+v.encode("utf-8")+"'" + " and "

        sql = 'update '+table+' set ' + da.strip(',') + ' where '+wr.rstrip(" and ")
        print sql
        self.cusor.execute(sql)

    def add(self, table, data, rowkey):
        keys = []
        values = []
        for key, value in data.items():
            if not value:
                value = ""
            keys.append(key.encode("utf-8"))
            values.append("'"+value.encode("utf-8")+"'")
        if rowkey:
            for k, v in rowkey.items():
                keys.append(k)
                values.append("'"+v+"'")
        sql = "insert into "+table+" ("+",".join(keys)+") values ("+",".join(values)+")"
        self.cusor.execute(sql)

    def find(self, table, data, *args):
        # args为需要查询的字段
        wr = ""
        for k, v in data.items():
            wr += k.encode("utf-8")+"='"+v.encode("utf-8")+"'" + " and "
        sql = "select "+','.join(args)+" from "+table+" where " + wr.rstrip(" and ")
        print sql
        self.cusor.execute(sql)
        dat = self.cusor.fetchall()
        nres = []
        if dat:
            for i in dat:
                dic = {}
                for j in range(0, len(args)):
                    dic[args[j]] = i[j]
                nres.append(dic)
        return nres






