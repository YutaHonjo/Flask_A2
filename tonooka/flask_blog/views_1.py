from flask_blog import app #flask_blogの中のappを持ってくる
from flask import request,redirect,url_for,render_template,flash,session
from flask_blog import app

@app.route('/input', methods=['GET', 'POST'])
def input():
    # ここにinput.htmlを表示するためのコードを書く
    return render_template('input.html')

@app.route('/')
def show_entries():
    if not session.get('logged_in'):
        return redirect(url_for('input')) 
    return render_template('entries/input.html')
