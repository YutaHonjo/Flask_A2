#アプリケーションの本体ファイルを作成
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app =Flask(__name__) #Flaskのアプリケーション本体を作成
app.config.from_object('holiday.config')  #flask_blofフォルダ内のconfig.pyの内容をconfigとして扱う宣言

db = SQLAlchemy(app)

from holiday.view import input ,list  #必要