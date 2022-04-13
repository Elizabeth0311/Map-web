import os        # 보안로그인 
from flask import Flask, jsonify, request, render_template, make_response
from flask_login import  LoginManager, current_user, login_required, login_user, logout_user
from map_view import map 
from flask_cors import CORS


# https만 지원하는 기능을 http에서 테스트 할 때 필요한 설정
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1"

app = Flask(__name__,static_url_path='/static')

CORS(app)

# 서버 보안  # 랜덤설정시 session 리셋됨
app.secret_key = 'hyeri_server'  

# map_view/map.py 안에 Blueprint 객체 등록
app.register_blueprint(map.map_bp, url_prefix='/')  

# flask 라이브러리 
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'   # session 보호

@login_manager.user_loader
def load_user(user_id) :         # 함수정의
    return User.get(user_id)     # 아이디를 mysql에 저장, 객체로 반환.

@login_manager.unauthorized_handler
def unauthorized() :
     return make_response(jsonify(success=False), 401)


if __name__ == "__main__":              
    app.run(host="0.0.0.0", port="8080", debug=True)
    

