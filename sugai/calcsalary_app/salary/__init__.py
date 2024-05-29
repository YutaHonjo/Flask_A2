#アプリケーションの本体ファイルを作成
from flask import Flask
app =Flask(__name__) #Flaskのアプリケーション本体を作成
app.config.from_object('salary.config')  #flask_blofフォルダ内のconfig.pyの内容をconfigとして扱う宣言

import  salary.views