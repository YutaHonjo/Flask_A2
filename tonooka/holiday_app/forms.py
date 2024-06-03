from flask_wtf import FlaskForm
from wtforms import DateField, StringField, SubmitField
from wtforms.validators import DataRequired

class HolidayForm(FlaskForm):
    holi_date = DateField('Date', validators=[DataRequired()])
    holi_text = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')