from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.mst_holiday import Holiday


@app.route('/', methods=['GET', 'POST'])
def input():
    return render_template('input.html')


@app.route('/input', methods=['POST'])
def add_holiday():
    holiday = Holiday(
        title=request.form['title'],
        text=request.form['text']
    )
    db.session.add(holiday)
    db.session.commit()
    flash('が登録されました')
    return redirect(url_for('show_entries'))