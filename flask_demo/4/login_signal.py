#! /usr/bin/env python
# coding=utf-8
from flask import Flask, request, redirect, url_for
import flask_login
from flask_sqlalchemy import SQLAlchemy
'''
flask_login中信号的例子
pip install flask_login
pip install flask_sqlalchemy
pip install pymysql
pip install blinker
'''
app = Flask(__name__)
app.secret_key = 'super secret string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:dgbuaa@mysql:3306/flask'

db = SQLAlchemy(app)

login_manager = flask_login.LoginManager()
login_manager.init_app(app)


password = '123'

# flask_login.UserMixin提供一些是否验证，是否激活，是否匿名用户，等属性
class User(flask_login.UserMixin, db.Model):
    __tablename__ = 'login_users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    login_count = db.Column(db.Integer, default=0)
    last_login_ip = db.Column(db.String(128), default='unknown')

# 创建数据库表
# 之前还是导入数据库文件的，现在是orm直接创建
db.create_all()

# user_logged_in绑定的函数
@flask_login.user_logged_in.connect_via(app)
def _track_logins(sender, user, **extra):
    user.login_count += 1
    user.last_login_ip = request.remote_addr
    db.session.add(user)
    db.session.commit()


@login_manager.user_loader
def user_loader(id):
    user = User.query.filter_by(id=id).first()
    return user


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return '''
<form action='login' method='POST'>
    <input type='text' name='name' id='name' placeholder='name'></input>
    <input type='password' name='pw' id='pw' placeholder='password'></input>
    <input type='submit' name='submit'></input>
</form>
               '''

    name = request.form.get('name')
    if request.form.get('pw') == password:
        user = User.query.filter_by(name=name).first()
        if not user:
            user = User(name=name)
            db.session.add(user)
            db.session.commit()
        flask_login.login_user(user)# 会引起@login_manager.user_loader和@flask_login.user_logged_in.connect_via(app)活动？
        return redirect(url_for('protected'))

    return 'Bad login'


@app.route('/protected')
@flask_login.login_required # 应该不是信号，没有connect,应该是用来传递登陆后的信息的 
def protected():
    user = flask_login.current_user
    return 'Logged in as: {}| Login_count: {}|IP: {}'.format(
        user.name, user.login_count, user.last_login_ip)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
