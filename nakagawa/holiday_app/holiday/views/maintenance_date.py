from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.mst_holiday import Holiday
from holiday.views.input import show_holiday

# 各メンテナンス
@app.route('/maintenance_date', methods = ['POST'])
def maintenance_holiday():
    # 入力した値
    holi_date_input = request.form.get('holi_date')
    # データベースから同じ日付があるか確認
    holiday = Holiday.query.get(holi_date_input)
    #新規登録・更新ボタンが押されたとき
    if request.form['button'] == 'insert_update':
        #同じ日付があるとき
        if holiday:
            holiday.holi_date = request.form.get('holi_date')
            holiday.holi_text = request.form.get('holi_text')
            #データベース更新
            db.session.merge(holiday)
            db.session.commit()
            message =  f'{holiday.holi_date }は「{ holiday.holi_text }」に更新されました'
        #同じ日付がないとき
        else:
            holiday = Holiday(
                holi_date = request.form.get('holi_date'),
                holi_text = request.form.get('holi_text')
            )
            #データベース追加
            db.session.add(holiday)
            db.session.commit()
            message =  f'{holiday.holi_date }（{ holiday.holi_text }）が登録されました'
    #削除ボタンが押されたとき
    elif request.form['button'] == 'delete':
        if not holiday:
            error_text = f'{holi_date_input}は、祝日マスタに登録されていません'
            flash(error_text)
            return redirect(url_for('show_holiday'))
        else:
        #データベース削除
            db.session.delete(holiday)
            db.session.commit()
            message = f'{ holiday.holi_date }（{ holiday.holi_text }）は削除されました'
    # 結果画面（result.htmlを返す）
    return render_template('result.html', message = message)


