#ビューファイルの作成(処理内容を記載)

from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from functools import wraps
from holiday.model.mst_holiday import Holiday
from holiday import db
from datetime import datetime
"""
def login_required(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return view(*args, **kwargs)
    return inner
"""
#入力祝日がデータベースにあるかどうかの判別関数(yにはrequest.form)
def discriminant(y):
    print('aaaaaaaa')
    print(y)
    print(type(Holiday.query.first().holi_date),type(y))
    #queryのやつとyは型が違うから（前者がdatetime,後者がstr）揃える必要ある
    print((datetime.strptime(str(Holiday.query.first().holi_date),'%Y-%m-%d').strftime('%Y-%m-%d'))==datetime.strptime(
        y,'%Y-%m-%d').strftime('%Y-%m-%d'))
    #print((datetime.strptime(str(Holiday.query.first().holi_date),'%Y-%m-%d').strftime('%Y-%m-%d'))==datetime.strptime(y,'%Y-%m-%d').strftime('%Y-%m-%d'))

    return Holiday.query.filter_by(holi_date = y).first()


#ルートに接続したときにinput.htmlを表示する
@app.route('/', methods=['GET', 'POST'])
def a():
    if request.method =='GET':
        return render_template('/input.html')

@app.route('/iii', methods=['GET', 'POST'])
def b():
    if request.method =='POST':
        #「新規登録・更新」ボタンを押したとき
        if request.form["button"] == "insert_update":
            #(1)入力されたのがデータベースに登録されてない場合は入力の日付、テキストを新規登録し、結果画面に遷移
            #(2)入力が登録されていたら入力の日付、テキストを更新し、結果画面に遷移
            x = discriminant(request.form['holiday'])
            #(1)の処理         
            if x is True:
                print('aaaaa')
                entry = Holiday(holi_date=request.form['holiday'], holi_text=request.form['holi_text'])
                db.session.add(entry)
                db.session.commit()
                print("存在してる")
                return render_template('/result.html')
            #(2)の処理
            else:
                print("存在してない")
                return render_template('/result.html')


            print("f")
        
        elif request.form["button"] == "delete":
            #入力が登録されてたらデータベースのレコードを削除し、結果画面に遷移
            #入力が登録されてなかったら”登録されていません”のフラッシュメッセージを出力
            print("t")

        elif request.form["button"] == "show":
            #一覧出力ボタンを押したら出力画面に遷移

            print("s")
            return render_template('/list.html')
            


    


    


"""
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method =='POST':  #「ログイン」ボタンを押したとき
        if request.form['username']!=app.config['USERNAME']:
            flash('ユーザー名が異なります')
        elif request.form['password']!=app.config['PASSWORD']:
            flash('パスワードが異なります')
        else:
            session["logged_in"] = True
            flash("ログインしたよ！！")
            return redirect(url_for("show_entries"))
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    flash("ログアウト！！！！")
    return redirect(url_for("show_entries"))
"""
# #入力が祝日かどうかを判断するプログラム
# holidaylist=Holiday.session.query.all()
# a = []
# for holiday in holidaylist:
#     a.append(holiday.holi_date)
#     print(a)
# if dt in a:
#     pay_sum=2400*input2 + 1500*input3
# elif dt.strftime("%a") == "Sat" or dt.strftime("%a") == "Sun":
#     pay_sum=2400*input2 + 1500*input3
# else:
#     pay_sum=2000*input2 + 1200*input3


