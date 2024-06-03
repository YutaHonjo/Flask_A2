from flask_sqlalchemy import SQLAlchemy
from flask import Flask ,render_template,request,redirect,url_for

app = Flask(__name__)

#既存のデータベースに接続
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite://holiday.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

#モデルを定義
class Holiday(db.Model):
    __tablename__ = 'holiday'
    holi_date = db.Column(db.Date, primary_key=True)
    holi_text = db.Column(db.String(20), unique=True)
    # text = db.Column(db.Text)


    def __init__(self, holi_date=None, holi_text=None):
        self.holi_date = holi_date
        self.holi_text = holi_text

    def __repr__(self):
        return '<Holiday holi_date:{} holi_text:{}>'.format(self.holi_date, self.holi_text)
    
