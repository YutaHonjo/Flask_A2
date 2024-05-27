#アプリケーションの本体ファイルを作成
from flask import Flask
app =Flask(__name__)

import flask_blog.views
