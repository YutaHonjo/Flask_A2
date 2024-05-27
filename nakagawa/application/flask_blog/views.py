from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app

#リンクが開かれた（リクエストがあった）ときの処理
@app.route('/')
def show_entries():
    return render_template('entries/index.html')