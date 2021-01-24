from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app

@app.route('/')
def show_entries():
    # セッションでlogged_inがTrueでない場合はログイン画面にリダイレクトしている
    if not session.get('logged_in'):
        return redirect('/login')
    return render_template('entries/index.html')

@app.route('/login', methods={'GET', 'POST'})
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            # flashにmessageを格納する
            flash('ユーザ名が異なります')
        elif request.form['password'] != app.config['PASSWORD']:
            flash('パスワードが異なります')
        else:
            # セッションにlogged_in=Trueを渡す
            session['logged_in'] = True
            flash('ログインしました')
            return redirect(url_for('show_entries'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    # ログアウト時、セッションのlogged_inをNoneに更新する
    session.pop('logged_in', None)
    flash('ログアウトしました')
    return redirect(url_for('show_entries'))