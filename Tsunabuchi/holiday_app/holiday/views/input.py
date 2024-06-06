from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.mst_holiday import Holiday


@app.route('/', methods=['GET', 'POST'])
def input():
    return render_template('input.html')