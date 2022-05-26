from flask import Blueprint, redirect, request , render_template, url_for, session
from map_control.user_mgmt import User
from flask_login import login_user, current_user


map_bp = Blueprint('map',__name__)

# 메인화면 
@map_bp.route("/",methods=['GET','POST'])  
def in_user():
    if request.method == "GET" :
        # print(request.args.get("web_id")
        return redirect(url_for('map.map_in'))    # "http://127.0.0.1:8080 접속시 나오는 화면"
    else  :
        # print(request.form['web_id'])
        # print('0', request.headers)
        session.permanent = True           
        user = User.create(request.form["web_id"],request.form["user_pw"], "A")  
        # login_user(user,force = True)
        
        return redirect(url_for('map.map_in'))
           
        
# 사용자 등록 후 
@map_bp.route("/map_in")
def map_in() :
    if current_user.is_authenticated :
        return render_template("map.html", web_id = current_user.web_id)
    else : 
        return render_template("map.html")



# 회원가입 후
# @map_bp.route("/signup",methods=['GET','POST'])    
# def signup() :
#     print('signup', request.form["web_id"],request.form["user_pw"])
    # user = User.create(request.form["web_id"],request.form["user_pw"], "A")  
    # print(user)
    # login_user(user)
    # return render_template("map_in.html")

# 로그인 후
# @map_bp.route("/login",methods=['GET','POST'])
# def login() :
#     if current_user.is_authenticated :
#         return render_template("map_in.html", web_id = current_user.web_id)
#     else : 
#         return render_template("map.html")

# 지도 화면으로 바로 들어올 경우
# @map_bp.route("/in", methods= ["GET","POST"])
# def map() :
#     if request.method == "GET" : 
#         return render_template("map.html")
#     else : 
#         return redirect(url_for("map.login"))
        

# redirect(url_for("map.map_page"))    # url_for(bp별칭.라우팅함수명)
# return redirect("/map")                   # url_for 안쓸경우 