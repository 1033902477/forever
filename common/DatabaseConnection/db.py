import pymysql

class db():
    def DbConnection(self):
        db = pymysql.connect(host='',
                             user='',
                             password='',
                             port=3306,
                             db='test',
                             charset='utf8'
                             )
        cursor = db.cursor()

        return cursor