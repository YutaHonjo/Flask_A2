from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.mst_holiday import Holiday

@app.route('/', methods = ['GET'])
def show_holiday():
    return render_template('input.html')

@app.route('/', methods = ['POST'])
def store_update_holiday():
    holi_date_input = request.form.get('holiday')
    holiday = Holiday.query.get(holi_date_input)
    print(holiday)
    if holiday:
        holiday.holi_date = request.form.get('holi_date')
        holiday.holi_text = request.form.get('holi_text')
        db.session.merge(holiday)
    else:
        holiday = Holiday(
            holi_date = request.form.get('holiday'),
            holi_text = request.form.get('holi_text')
        )
        db.session.add(holiday)
    db.session.commit()
    return render_template('result.html', holiday = holiday)
