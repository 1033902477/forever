import pymysql

# 数据库连接的时候可以调用公共类方法进行连接
class db():
    def DbConnection(self):
        db = pymysql.connect(host='', user='', password='', port=3306, db='test', charset='utf8')
        cursor = db.cursor()
        return cursor