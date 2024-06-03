from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#アプリケーション本体の作成
app = Flask(__name__)
app.config.from_object('holiday.config')

db = SQLAlchemy(app)

from holiday.views import input, maintenance_date, list