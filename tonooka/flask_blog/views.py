from flask_blog import app #flask_blogの中のappを持ってくる
from flask import request,redirect,url_for,render_template,flash,session
import math
from flask import flash

#server.pyが実行された際の一番最初のページを定義
@app.route('/')
def show_entries():
    if not session.get('logged_in'):
        return redirect(url_for('input')) 
    return render_template('input.html')

@app.route('/input', methods=['GET', 'POST'])
def input():
    if request.method == 'POST':
        salary = request.form['salary']
        if not salary:
            flash('給料が未入力です。入力してください')
            return render_template('input.html')
        salary = int(salary)
        if salary < 0:
            flash('給料にはマイナスの値は入力できません')
            return render_template('input.html')
        if len(str(salary)) > 10:
            flash('給料には最大9999999999まで入力可能です。')
            return render_template('input.html')
        if salary > 1000000:
            tax = round((1000000 * 0.1) + ((salary - 1000000) * 0.2))
        else:
            tax = round(salary * 0.1)
        payment = salary - tax
        return render_template('output.html',salary=salary, payment=payment, tax=tax)
    return render_template('input.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            print('ユーザ名が異なります')
        elif request.form['password'] != app.config['PASSWORD']:
            print('パスワードが異なります')
        else:
            session['logged_in'] = True
            flash('ログインしました')
            return redirect(url_for('show_entries'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('ログアウトしました')
    return redirect(url_for('show_entries'))