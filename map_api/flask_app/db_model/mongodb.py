import pymongo 

MONGO_HOST = 'localhost'
MONGO_CONN = pymongo.MongoClient('mongodb://%s' % (MONGO_HOST))

def conn_mongodb() :
    try :
        MONGO_CONN.admin.command('ismaster')
        map_api = MONGO_CONN.map_session_db.map_api
    except :
        MONGO_CONN = pymongo.MongoClient('mongodb://%s' % (MONGO_HOST))
        map_api = MONGO_CONN.map_session_db.map_api
    return map_api