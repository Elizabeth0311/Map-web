from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index() :
    return render_template('map.html')

# @app.route('/', methods=['GET','POST'])
# def index():
#     return render_template('map.html')