import pymysql

# 数据库连接的时候可以调用公共类方法进行连接
class Db():
    def db(self):
        db = pymysql.connect(host='localhost', user='root', password='', port=3306, db='test', charset='utf8')

        return db


if __name__=='__main__':
    db = Db().db()
    cur = db.cursor()
    # insql = '''insert into `test`.`new_table` (`username`, `password`) values ('123456789', '12345678')'''
    # cur.execute(insql)
    # db.commit()
    # db.close()
    result=None

    try:
        sql = '''select * from `test`.`new_table` where username = '123456789' '''
        cur.execute(sql)
        result = cur.fetchone()
    except Exception as e:
        print(e)
        db.rollback()

    print(result)