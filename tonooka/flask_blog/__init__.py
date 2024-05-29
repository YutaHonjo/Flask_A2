#アプリケーション本体のファイルの作成
from flask import Flask

app = Flask(__name__)#Flaskのアプリケーションを作成

app.config.from_object('flask_blog.config')#flask_blogフォルダの中のconfigファイルのdebug=trueをアプリ内で行う
                                           #いちいちpython〇〇って打たなくてもずっと実行し続けてくれる

import flask_blog.views #これから作成するviewsファイルをインポートする


