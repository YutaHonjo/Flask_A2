from flask import request, request, redirect, url_for, render_template, flash, session
from flask_blog import app
from werkzeug.exceptions import Unauthorized

@app.route('/')
def show_entries():
    # if not session.get('logged_in'):
    #     return redirect(url_for('login'))
    return render_template('entries/index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            flash('ユーザ名が異なります','danger')
        elif request.form['password'] != app.config['PASSWORD']:
            flash('パスワードが異なります','danger')
        else:
            session['logged_in']=True
            flash('ログインしました','info')
            return redirect(url_for('show_entries'))
    return render_template('entries/login.html')


@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    flash('ログアウトしました','info')
    return redirect(url_for('show_entries'))

@app.errorhandler(Unauthorized)
def handle_unauthorized(e):
    return redirect(url_for('login'))