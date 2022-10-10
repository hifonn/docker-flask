from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR   # MySQLのテーブルを作る時に必要
import pymysql

#内部処理
app = Flask(__name__)

app.config.from_object('config')

import views

db = SQLAlchemy(app)
from models import user

if __name__ == '__main__':
    app.run(host='localhost')
