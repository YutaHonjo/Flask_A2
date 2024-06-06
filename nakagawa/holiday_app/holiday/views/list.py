from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.mst_holiday import Holiday

# 各メンテナンス
@app.route('/list', methods = ['GET'])
def list_holiday():
    holidays = Holiday.query.all()
    return render_template('list.html', holidays = holidays)