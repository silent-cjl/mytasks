import pymysql

# mysql_coon 主要的功能就是, 将链接数据库的操作变成只连接一次
#
class mysql_conn(object):
    # 魔术方法, 初始化, 构造函数
    def __init__(self):
        self.db = pymysql.connect(host='127.0.0.1', user='root', password='abc123', port=3306, database='py1011')
        self.cursor = self.db.cursor()
    # 执行modify(修改)相关的操作
    def execute_modify_mysql(self, sql):
        self.cursor.execute(sql)
        self.db.commit()
    # 魔术方法, 析构化 ,析构函数
    def __del__(self):
        self.cursor.close()
        self.db.close()



if __name__=='__main__':
    sql = 'insert into xueqiu_test values (3)'
    mc = mysql_conn()
    mc.execute_modify_mysql(sql)
    sql = 'insert into xueqiu_test values (4)'
    mc.execute_modify_mysql(sql)
    sql = 'insert into xueqiu_test values (5)'
    mc.execute_modify_mysql(sql)
    sql = 'insert into xueqiu_test values (6)'
    mc.execute_modify_mysql(sql)

