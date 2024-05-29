#hello.py

from flask import Flask #flaskモジュールからFlaskをインポート
app = Flask(__name__) #flaskクラスのインスタンスを作成し、変数appに割り当てる
                      #__name__は特殊な変数　Flaskがどこから実行されているのかをFlaskに伝える　

@app.route('/')
def hello_world():
    return "Hello Worssld!"

def print_test():
    print('hello')

if __name__=='__main__':  # __name__を書くことでほかのファイルで表示する際に、確立することができる。
    app.run()