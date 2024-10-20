from flask import Flask
#initialiser l'appli
def create_app():
    app = Flask(__name__)
     #encrypter et securiser les cookies du site
    app.config["SECRET_KEY"] = 'theKey' 
    
    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix = '/')
    app.register_blueprint(auth,url_prefix = '/')

    return app

