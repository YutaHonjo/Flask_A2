from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Holiday(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    holi_date = db.Column(db.Date, nullable=False)
    holi_text = db.Column(db.String(100), nullable=False)