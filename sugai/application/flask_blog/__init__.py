#アプリケーションの本体ファイルを作成
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app =Flask(__name__) #Flaskのアプリケーション本体を作成
app.config.from_object('flask_blog.config')  #flask_blofフォルダ内のconfig.pyの内容をconfigとして扱う宣言

db = SQLAlchemy(app)

from flask_blog.views import views, entries


