
from db_model.mongodb import conn_mongodb
from datetime import datetime

class MapSession() :
    map_page = {"A" : "map_A", "B" : "map_B.html"}
    session_count = 0
    
    @staticmethod
    def save_session_info(session_ip, web_id, webpage_name) :  # 접속시 <
        now = datetime.now()
        now_time = now.strftime("%d/%m/%Y %H:%M:%S") # strftime.org

        mongo_db = conn_mongodb()
        mongo_db.insert({
            'session_ip' : session_ip,
            'web_id' : web_id,
            'page' : webpage_name,
            'access_time' : now_time
        })
    
    # 페이지 불러오기   
    @staticmethod
    def get_map_page(map_id=None) :
        if map_id == None :
            if MapSession.session_count == 0 :
                MapSession.session_count = 1
                return 'map_A.html'
        else :
            return MapSession.map_page[map_id]
            