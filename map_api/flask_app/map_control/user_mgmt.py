
from flask_login import UserMixin
from db_model.mysql import conn_mysqldb  #사용자 데이터 처리,  DB변경시 이부분 바꿔주면됨

class User(UserMixin) :
    
    def __init__(self, user_id, web_id, user_pw, map_id) :
        self.id = user_id  # self.id attributor는 flask_login에서 접근하기 때문에 변경시 에러남
        self.web_id = web_id
        self.user_pw = user_pw
        self.map_id = map_id

    def get_id(self):          # flask_login 사용시 반드시 추가해야함
        return str(self.id) 
    
    
    # user_id로 이용자 검색 
    @staticmethod
    def get(user_id) :  
        mysql_db = conn_mysqldb()        # 연결된 mysql호출
        db_cursor = mysql_db.cursor()    # cursor 호출 
        sql = "SELECT * FROM user_info WHERE USER_ID = ' " + str(user_id) + " ' "
        # print(sql)  sql문은 한번에 실행이 잘 안되므로 출력해보거나 workbench, 터미널에서 확인 후 코드작성
        db_cursor.execute(sql)       # mysql 실행 
        user = db_cursor.fetchone()  # user_id에 매칭되는 아이디는 하나(fetchone)
        
        if not user :             # 해당 데이터가 없으면
            return None           # 아무것도 반환하지 않음 
         
        user = User(user_id=user[0], web_id=user[1], user_pw = [2], map_id=[3])   # DB 컬럼 순서. Line22 에서 가져오는것
        return user
    
    # web_id로 이용자 검색
    @staticmethod
    def find(web_id) :  
        mysql_db = conn_mysqldb()        
        db_cursor = mysql_db.cursor()   
        sql = "SELECT * FROM user_info WHERE USER_ID = ' " + str(web_id) + " ' "
        db_cursor.execute(sql)
        user = db_cursor.fetchone()  
        if not user :             
            return None           
         
        user = User(user_id=user[0], web_id=user[1], user_pw = [2], map_id=[3])   
        return user
    
    # 새로운 이용자 저장 , 중복된 web_id가 mysql에 들어가지 않도록 함
    @staticmethod
    def create(web_id, user_pw, map_id) :
        user = User.find(web_id)          # 사용자 검색해보고 
        if user == None :                 # 사용자가 없을 경우    
            mysql_db = conn_mysqldb()        
            db_cursor = mysql_db.cursor()   
            sql = "INSERT INTO user_info (WEB_ID, USER_PW, MAP_ID) VALUES ('%s', '%s','%s') " % (str(web_id), str(user_pw), str(map_id)) 
            db_cursor.execute(sql)
            mysql_db.commit()           # 새로운 데이터 처리시 commit 
            return User.find(web_id)    # 다시 web_id를 검색해서 user_id 찾기
        else : 
            return user                 # 있을 경우 검색한 user 정보 반환 