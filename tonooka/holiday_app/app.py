from flask import Flask, render_template, request, redirect, url_for
from models import db, Holiday
from forms import HolidayForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///holiday.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)

@app.route('/')
def index():
    holidays = Holiday.query.all()
    return render_template('index.html', holidays=holidays)

@app.route('/new', methods=['GET', 'POST'])
def new_holiday():
    form = HolidayForm()
    if form.validate_on_submit():
        new_holiday = Holiday(holi_date=form.holi_date.data, holi_text=form.holi_text.data)
        db.session.add(new_holiday)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('new.html', form=form)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_holiday(id):
    holiday = Holiday.query.get_or_404(id)
    form = HolidayForm(obj=holiday)
    if form.validate_on_submit():
        holiday.holi_date = form.holi_date.data
        holiday.holi_text = form.holi_text.data
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', form=form)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_holiday(id):
    holiday = Holiday.query.get_or_404(id)
    db.session.delete(holiday)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

 