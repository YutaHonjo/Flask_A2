#Flaskアプリケーションのプログラムの実行が開始される場所
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import HolidayForm
from models import db, Holiday
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# データベースの初期化
# with app.app_context():
#     db.create_all()

@app.route('/')
def index():
    holidays = Holiday.query.all()
    return render_template('index.html', holidays=holidays)

@app.route('/new', methods=['GET', 'POST'])
def new_holiday():
    form = HolidayForm()
    if form.validate_on_submit():
        existing_holiday = Holiday.query.get(form.holi_date.data)
        if existing_holiday:
            existing_holiday.holi_text = form.holi_text.data
        else:
            new_holiday = Holiday(holi_date=form.holi_date.data, holi_text=form.holi_text.data)
            db.session.add(new_holiday)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('new.html', form=form)

@app.route('/edit/<string:holi_date>', methods=['GET', 'POST'])
def edit_holiday(holi_date):
    holiday = Holiday.query.get_or_404(holi_date)
    form = HolidayForm(obj=holiday)
    if form.validate_on_submit():
        holiday.holi_date = form.holi_date.data
        holiday.holi_text = form.holi_text.data
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', form=form)

@app.route('/delete/<string:holi_date>', methods=['POST'])
def delete_holiday(holi_date):
    holiday = Holiday.query.get_or_404(holi_date)
    db.session.delete(holiday)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)