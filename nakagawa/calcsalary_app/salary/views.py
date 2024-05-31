from flask import request, redirect, url_for, render_template, flash, session
from salary import app
from decimal import Decimal, ROUND_HALF_UP


@app.route('/')
def show_input():
    return render_template('entries/error.html')

@app.route('/', methods=['POST'])
def show_error():
    if request.form['salary'] == '':
        flash('給与が未入力です。入力してください。')
        return render_template('entries/input.html')
    elif len(request.form['salary']) > 10:
        flash('給与には最大9,999,999,999まで入力可能です。')
        return render_template('entries/error.html', error_int = request.form['salary'])
    return render_template('entries/input.html')
    

@app.route('/output', methods=['POST'])
def show_output():
    input_salary = int(request.form['salary'])
    if input_salary >= 1000000:
        tax = (input_salary - 1000000) * 0.2 + 1000000 * 0.1
    else:
        tax = input_salary * 0.1
    tax = Decimal(str(tax)).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
    allowance = input_salary - tax
    re_input_salary = '{:,}'.format(input_salary)
    re_allowance = '{:,}'.format(allowance)
    re_tax = '{:,}'.format(tax)
    result = f'給与：{re_input_salary}円の場合、支給額：{re_allowance}円、税額：{re_tax}円です。'
    return render_template('entries/output.html', salary=result)
