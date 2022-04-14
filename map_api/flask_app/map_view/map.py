from crypt import methods
from flask import Blueprint, Flask, redirect, request , render_template, url_for

map_bp = Blueprint('map',__name__)


@map_bp.route("/",methods=['GET','POST'])  # POST만 지정할 시 에러발생, GET 추가해야함
def login_page():
    if request.method == "POST" :
        return redirect(url_for("map"))
    return render_template('login.html')

@map_bp.route("/map",methods=["GET","POST"])
def map_page():
    return render_template('map.html')

