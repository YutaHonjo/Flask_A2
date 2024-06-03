#既存のデータベースに接続するため
import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///holidays.db'  # データベースのURIを指定
    SECRET_KEY = '111'
    SQLALCHEMY_TRACK_MODIFICATIONS = False



