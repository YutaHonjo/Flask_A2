from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#アプリケーション本体の作成
app = Flask(__name__)
app.config.from_object('flask_blog.config')

db = SQLAlchemy(app)

from flask_blog.views import views, entries