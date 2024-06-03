from flask import request, redirect, url_for, render_template, flash, session
from flask import Flask, render_template, request
from holiday import app
import holiday
from holiday import db



@app.route('/')
def show_entries():
    return render_template('input.html')


@app.route('/input', methods=['GET','POST'])
def input():
    holiday = None
    holiday_text = None
    if request.method == 'POST':
        if request.form["button"] == "insert_update":
            holiday = request.form.get('holiday')
            holiday_text = request.form.get('holiday_text')
            # ここでデータベースに保存するなどの処理を行う
            return render_template('shinki.html', holiday=holiday, holiday_text=holiday_text)

@app.route('/shinki',methods=['GET', 'POST'])
def ank():
    return render_template('input.html')

@app.route('/entries/new', methods=['GET'])
def new_entry():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('entries/new.html')




