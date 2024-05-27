#ビューファイルの作成(処理内容を記載)
from flask_blog import app

@app.route('/')
def show_entries():
    return "Hello World!!!"