from flask import Flask, request, redirect
from flask_mysqldb import MySQL


mysql = MySQL()
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dseffs'
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'RZ1mysql'
    app.config['MYSQL_DB'] = 'university'

    mysql.init_app(app)

    from .views import views
    #from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    #app.register_blueprint(auth, url_prefix='/')

    return app




