from flask import Blueprint, Flask, request , render_template

map_bp = Blueprint('map',__name__)


@map_bp.route("/login")
def login_page():
    return render_template('login.html')

@map_bp.route("/login/map")
def main_page():
    return render_template('main_map.html')

