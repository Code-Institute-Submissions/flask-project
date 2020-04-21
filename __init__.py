# #The Application Factory
# #__init__py tells Python that the mainapp directory should be treated as a package.
# from flask import Flask
# #from flask_login import LoginManager
# #from db import db
# #from flask_migrate import Migrate
# from flask_bootstrap import Bootstrap
# #from config import app_config
# #from flask_migrate import Migrate
# from flask_session import Session

# #https://hackersandslackers.com/flask-blueprints
# #sess = Session()
# #login_manager = LoginManager()
# from flask_login import LoginManager

# app = Flask(__name__)
# # ...
# login = LoginManager(app)

# #static_folder="static", template_folder="templates"


# def create_app(config_name):  #create_app is the application factory function.
#     app =Flask(__name__)#app = Flask(__name__, instance_relative_config=True) creates the Flask instance.__name__ is the name of the current Python module. The app needs to know where it’s located to set up some paths, and __name__ is a convenient way to tell it that.
#     app.config.from_pyfile(config_name) #app.config.from_pyfile() overrides the default configuration with values taken from the config.py file in the instance folder if it exists. For example, when deploying, this can be used to set a real SECRET_KEY.test_config can also be passed to the factory, and will be used instead of the instance configuration. This is so the tests you’ll write later in the tutorial can be configured independently of any development values you have configured.

#     #from app import models

#     from .admin import admin as admin_blueprint
#     app.register_blueprint(admin_blueprint, url_prefix='/admin')

#     from .auth import auth as auth_blueprint
#     app.register_blueprint(auth_blueprint)

#     from .home import home as home_blueprint
#     app.register_blueprint(home_blueprint)

#     #Bootstrap(app)
#     #db.__init__(app)

#     from . import auth
#     app.register_blueprint(auth.bp)

#     app =Flask(__name__, instance_relative_config=True)
#     app.config.from_pyfile('config.py')
#     #app.config.from_object(app_config[config_name])
#     app.config.from_object('config.Config') 
#     app.config['DEBUG'] = True
#     #login_manager.init_app(app)
#     #login_manager.login_message = ""
#     #login_manager.login_view ="auth.login"
    
     
#     #migrate = Migrate(app, connectDB)
    
#     return app