from flask import Flask
from flask.templating import render_template

app = Flask(__name__,static_url_path='/static')


@app.route("/main")
def main_page():
    return render_template('main_map.html')

@app.route("/login")
def login_page():
    return render_template('login.html')



if __name__ == "__main__":              
    app.run(host="0.0.0.0", port="8080")