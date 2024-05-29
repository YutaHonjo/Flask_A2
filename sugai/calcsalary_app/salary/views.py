from salary import app
from flask import request, redirect, url_for, render_template, flash, session
from decimal import Decimal, ROUND_HALF_UP
import re

@app.route('/', methods=['GET', 'POST'])  #http://127.0.0.1:5000/にリクエストがあった際に以下のdefメソッドが呼び出される
#給料を入力として支給額、税額を返す関数
def calcsalary():
    if request.method =='GET':
        return render_template('/input.html')

    if request.method =='POST':  #「ログイン」ボタンを押したとき


        input_salary = request.form['salary']
        if input_salary =="":
            flash("給与が未入力です。入力してください。")
            return render_template('/input.html')

        elif re.fullmatch('[0-9]+', input_salary) ==None:
            flash("給与にはマイナスの値は入力できません。")
            return render_template('/input.html', a = input_salary)
        elif len(input_salary) > 11:
            flash("給与には最大9,999,999,999まで入力可能です。")
            return render_template('/input.html',a = input_salary)

        else:
            input_salary=int(request.form['salary'])

            if input_salary > 1000000:
                surplus_minutes = input_salary - 1000000
                tax = 1000000*0.1 + surplus_minutes*0.2
                tax = Decimal(str(tax)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
                pay_amount = input_salary - tax 
            else:
                tax = input_salary * 0.1
                tax = Decimal(str(tax)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
                pay_amount = input_salary -tax
            return render_template('/output.html', input=input_salary, salary=pay_amount, tax=tax)
        


@app.route("/output", methods=['GET', 'POST'])
def output():
    if request.method =='POST':
        #return redirect('input.html')
        return render_template('/input.html')
        




    