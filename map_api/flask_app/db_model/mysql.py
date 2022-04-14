import pymysql

MYSQL_HOST = 'localhost'
MYSQL_CONN = pymysql.connect( 
        host=MYSQL_HOST,
        port=3306
        user='hyeri'
        passwd='moonhr'
        db='map_db'
        charset='utf8'
)


def conn_mysqldb():                 #mysql 커넥션
    if not MYSQL_CONN.open :        # 해당객체가 연결이 끊어지면
        MYSQL_CONN.ping(reconnect=True)   # 다시접속
    return MYSQL_CONN                    # 아닐 시 현재 연결된 객체 리턴