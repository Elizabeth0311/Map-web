from flask import Blueprint,render_template 


map_bp = Blueprint('map',__name__)

# 메인화면 
@map_bp.route('/',methods=['GET','POST'])  #http://127.0.0.1:8080/map
def index():
    return render_template("map_A.html")



# bp = Blueprint('main', __name__)

# @bp.route('/', methods=['GET', 'POST'])
# def index() :
#     return render_template('map.html')

# @app.route('/', methods=['GET','POST'])
# def index():
#     return render_template('map.html')
