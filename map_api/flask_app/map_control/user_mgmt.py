from flask_login import UserMixin
from db_model.mysql import conn_mysqldb


class User(UserMixin):

    def __init__(self, user_id, web_id, map_id):
        self.id = user_id
        self.web_id = web_id
        self.map_id = map_id

    def get_id(self):
        return str(self.id)

    @staticmethod
    def get(web_id):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT * FROM user_info WHERE web_id = '" + str(web_id) + "'"
        # print (sql)
        db_cursor.execute(sql)
        user = db_cursor.fetchone()
        if not user:
            return None

        user = User(user_id=user[0], web_id=user[1], map_id=user[2])
        return user

    @staticmethod
    def find(web_id):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT * FROM user_info WHERE WEB_ID = '" + \
            str(web_id) + "'"
        # print (sql)
        db_cursor.execute(sql)
        user = db_cursor.fetchone()
        if not user:
            return None

        user = User(user_id=user[0], web_id=user[1], map_id=user[2])
        return user

    @staticmethod
    def create(web_id, map_id):
        user = User.find(web_id)
        if user == None:
            mysql_db = conn_mysqldb()
            db_cursor = mysql_db.cursor()
            sql = "INSERT INTO user_info (WEB_ID, MAP_ID) VALUES ('%s', '%s')" % (
                str(web_id), str(map_id))
            db_cursor.execute(sql)
            mysql_db.commit()
            return User.find(web_id)
        else:
            return user

    @staticmethod
    def delete(web_id):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "DELETE FROM user_info WHERE WEB_ID = %d" % (web_id)
        deleted = db_cursor.execute(sql)
        mysql_db.commit()
        return deleted
