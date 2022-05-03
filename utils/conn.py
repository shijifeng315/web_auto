"""
python操作数据库
"""
import pymysql

db_info = {"host":"49.235.92.12",
           "user":"root",
           "password":"123456",
           "database":"apps",
           "port":3309}

class ConnectDB():

    def __init__(self,db_info):
        self.db = pymysql.connect(**db_info,
                                  cursorclass=pymysql.cursors.DictCursor,)

        #创建游标
        self.cur=self.db.cursor()

    def select_sql(self,sql):
        #定义一个查询数据库的函数
        self.cur.execute(sql)
        result = self.cur.fetchall()
        self.db.close()
        return result

    def execute_sql(self,sql):
        #定义一个对数据库进行增删改查的函数
        self.cur.execute(sql)
        self.db.commit()
        self.db.close()


if __name__ == '__main__':
    conn = ConnectDB(db_info)
    sql1 = 'SELECT * from auth_user WHERE username="test";'
    re1 = conn.select_sql(sql1)
    print(re1)
    sql2 = 'UPDATE auth_user set email="99999@qq.com"  where username="test";'
    # re2 = conn.execute_sql(sql2)    #去数据库查询是否修改成功




