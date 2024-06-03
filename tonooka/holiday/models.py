from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Holiday(db.Model):
        __tablename__ = 'holiday'
        holi_date = db.Column(db.Date, primary_key=True)
        holi_text = db.Column(db.String(20), unique=True)