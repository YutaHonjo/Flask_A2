from flask import Flask

#アプリケーション本体の作成
app = Flask(__name__)
app.config.from_object('flask_blog.config')
import flask_blog.views