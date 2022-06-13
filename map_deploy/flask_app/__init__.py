from flask import Flask, render_template 

def create_app() :
    app = Flask(__name__)
    
    # @app.route('/', methods=['GET','POST'])
    # def index():
    #     return render_template('map.html')
    
    from flask_app.views import main_view
    app.register_blueprint(main_view.map_bp)
    
    return app

if __name__ == "__main__" :
    app = create_app()
    app.run()    
