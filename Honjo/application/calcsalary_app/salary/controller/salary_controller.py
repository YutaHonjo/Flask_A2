from flask import request, request, redirect, url_for, render_template, flash, session
import math


def calc_form():
    return render_template('input.html')


def calc_result(salary):
    if not validation(salary):
        return render_template('input.html', old_salary=salary)
    salary = int(salary)
    tax = 0
    if salary > 1000000:
        over_million = salary-1000000
        tax += over_million*0.2
        tax += 1000000*0.1
        tax = math.floor(tax)
        payment = salary-tax
    else:
        tax = math.floor(salary*0.1)
        payment = salary-tax
    return render_template('output.html', salary=salary, payment=payment, tax=tax)


def validation(salary):
    if salary == '':
        flash('給与が未入力です。入力してください。')
    elif '.' in salary:
        flash('給与は整数を入力してください。')
    elif len(salary) > 10:
        flash('給与には最大9,999,999,999まで入力可能です。')
    elif int(salary) < 0:
        flash('給与にはマイナスの値は入力できません。')
    else:
        return True
