from flask import Flask
from flask.templating import render_template

app = Flask(__name__)


@app.route("/main")
def first_page():
    return render_template('main_map.html')



if __name__ == "__main__":              
    app.run(host="0.0.0.0", port="8080")