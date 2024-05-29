
from flask import request, request, redirect, url_for, render_template, flash, session
from salary import app
from werkzeug.exceptions import Unauthorized
from .controller import salary_controller

@app.route('/calc_salary',methods=['GET','POST'])
def calc_salary():
    if request.method=='POST':
        return salary_controller.calc_result(request.form.get('salary'))
    else:
        return salary_controller.calc_form()
    