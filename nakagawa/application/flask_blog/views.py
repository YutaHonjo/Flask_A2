from flask_blog import app

#リンクが開かれた（リクエストがあった）ときの処理
@app.route('/')
def show_entries():
    return 'Hello World!'