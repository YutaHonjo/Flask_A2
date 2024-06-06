#ビューファイルの作成(処理内容を記載)

from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from functools import wraps
from holiday.model.mst_holiday import Holiday
from holiday import db
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


#入力祝日がデータベースにあるかどうかの判別関数(yにはrequest.form)
def discriminant(y):
    return Holiday.query.filter_by(holi_date = datetime.strptime(y,'%Y-%m-%d')).first()



#ルートに接続したときにinput.htmlを表示する
@app.route('/', methods=['GET', 'POST'])
def a():
    if request.method =='GET':
        return render_template('/input.html')

@app.route('/iii', methods=['GET', 'POST'])
def b():
    holiday_date=request.form['holiday']
    holiday_text=request.form['holiday_text']
    #「新規登録・更新」ボタンを押したとき
    #(1)入力されたのがデータベースに登録されてない場合は入力の日付、テキストを新規登録し、結果画面に遷移
    #(2)入力が登録されていたら入力の日付、テキストを更新し、結果画面に遷移      
    if request.method =='POST':
        holiday = Holiday.query.get(holiday_date)
        if request.form["button"] == "insert_update":
            
            #(1)の処理
            if holiday is None:
                entry = Holiday(holi_date=holiday_date,holi_text=holiday_text)
                db.session.add(entry)
                db.session.commit()
                flag=1
                return render_template('/result.html',holiday_date=holiday_date, holiday_text=holiday_text, flag=flag)

            #(2)の処理
            else:
                entry = Holiday(holi_date=holiday_date,holi_text=holiday_text)
                db.session.merge(entry)
                db.session.commit()
                flag=2
                return render_template('/result.html',holiday_date=holiday_date, holiday_text=holiday_text, flag=flag)

        
        elif request.form["button"] == "delete":
            #入力が登録されてたらデータベースのレコードを削除し、結果画面に遷移
            #入力が登録されてなかったら”登録されていません”のフラッシュメッセージを出力
            if holiday is None:
                flash(holiday_date + "は、祝日マスタに登録されていません")
                flag=4
                return render_template('/input.html',flag=flag)
            else:
                db.session.delete(holiday)
                db.session.commit()
                print("t")
                flag=3
                return render_template('/result.html',holiday_date=holiday_date, holiday_text=holiday_text, flag=flag)
        #一覧出力ボタンを押したら出力画面に遷移
        elif request.form["button"] == "show":
            holidays = Holiday.query.all()
            return render_template('/list.html',holidays=holidays)
            
