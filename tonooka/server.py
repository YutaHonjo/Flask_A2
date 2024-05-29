# from flask_blog import app

# if __name__ =='__main__': #スクリプトが直接実行された場合のみに次のコードを実行する
#     app.run()             # app.run(debug=True) #debug = Trueはエラーが表示された際にデバッグ情報が表示される
#                             # コードが変更されると自動的にアプリケーションが再起動する

# from flask import Flask

# app = Flask(__name__)
# app.config.from_object('flask_blog.config')

from flask_blog import app

if __name__ == '__main__':
    app.run()

import flask_blog.views.entries