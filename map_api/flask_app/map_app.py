import os        # 보안로그인 프로토콜 
from flask import Flask, jsonify, request, render_template, make_response
from flask_login import  LoginManager, current_user, login_required, login_user, logout_user
from map_view import map 
from flask_cors import CORS
from map_control.user_mgmt import User

 

# https만 지원하는 기능을 http에서 테스트 할 때 필요한 설정
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1"

    
app = Flask(__name__,static_url_path='/static') # static_url_path='/static'

CORS(app)

app.secret_key = 'hyeri_server1' 

app.register_blueprint(map.map_bp, url_prefix = '/map') 


# 서버 보안  # 랜덤설정시 session 리셋됨
app.secret_key = 'hyeri_server'  


# flask 로그인매니져
login_manager = LoginManager()
login_manager.init_app(app)  # 로그인매니져에 플라스크 객체 등록 
login_manager.session_protection = 'strong'   # session 보호
 
# map_control/user_mgmt.py에서 import 
@login_manager.user_loader       # 사용자가 로그인 하면 세션을 관리 
def load_user(user_id) :         # 함수정의
    return User.get(user_id)     # 아이디를 mysql에 저장, 객체로 반환.
 
@login_manager.unauthorized_handler
def unauthorized() :                   # 로그인이 안된 사용자가 로그인이 된 사용자가 접근할 수 있는 요청을 했을 경우 함수호출
    return make_response(jsonify(success=False), 401)


if __name__ == "__main__":

    app.run(host='0.0.0.0', port= '8080', debug=True) 
    
    # EB 설정 
    # application.debug = True  # 디버그설정은 자유롭게 가능
    # application.run()         # 옵션 비워두기 (추천)

