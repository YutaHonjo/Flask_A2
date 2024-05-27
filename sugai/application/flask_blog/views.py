#ビューファイルの作成(処理内容を記載)
"""
from flask_blog import app

@app.route('/')  #http://127.0.0.1:5000/にリクエストがあった際に以下のdefメソッドが呼び出される
def show_entries():
    return "Hello World!!!"
"""

"""
from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app

@app.route("/")
def show_entries():
    return render_template('entries/index.html')
"""
from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app

@app.route('/')
def show_entries():
    return render_template('entries/index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method =='POST':
        if request.form['username']!=app.config['USERNAME']:
            print('ユーザー名が異なります')
        elif request.form['password']!=app.config['PASSWORD']:
            print('パスワードが異なります')
        else:
            return redirect("/")
    return render_template("login.html")

@app.route("/logout")
def logout():
    return redirect("/")



