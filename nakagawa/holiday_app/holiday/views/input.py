from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.mst_holiday import Holiday

# 入力画面（input.htmlを返す）
@app.route('/')
def show_holiday():
    return render_template('input.html')
