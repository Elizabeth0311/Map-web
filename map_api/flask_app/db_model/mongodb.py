import pymongo 

MONGO_HOST = 'localhost'
MONGO_CONN = pymongo.MongoClient('mongodb://%s' % (MONGO_HOST))  # %로 들어오는 값이 MONGO_HOST로 들어감

def conn_mongodb() :
    global MONGO_CONN
    try :
        MONGO_CONN.admin.command('ismaster')
        map_api = MONGO_CONN.map_session_db.map_api
    except :
        MONGO_CONN = pymongo.MongoClient('mongodb://%s' % (MONGO_HOST))
        map_api = MONGO_CONN.map_session_db.map_api
    return map_api