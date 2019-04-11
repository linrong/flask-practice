#! /usr/bin/env python
# coding=utf-8
import sys
sys.path.append('../common')
import os.path

from flask import Flask, redirect, url_for
from flask_admin import Admin
from flask_login import (current_user, UserMixin, LoginManager,
                         login_user, logout_user)
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.base import MenuLink, BaseView, expose


from ext import db
from users import User as _User
'''
pip install Flask-Admin
'''
app = Flask(__name__, template_folder='./templates',
            static_folder='./static')
app.config.from_object('config')
USERNAME = 'xiaoming'

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)


class User(_User, UserMixin):
    pass


@app.before_first_request
def create_user():
    db.drop_all()
    db.create_all()

    user = User(name=USERNAME, email='a@dongwm.com', password='123')
    db.session.add(user)
    db.session.commit()

# 给LINK增加条件
class AuthenticatedMenuLink(MenuLink):
    def is_accessible(self):
        return current_user.is_authenticated


class NotAuthenticatedMenuLink(MenuLink):
    def is_accessible(self):
        return not current_user.is_authenticated


@login_manager.user_loader
def user_loader(user_id):
    user = User.query.filter_by(id=user_id).first()
    return user


class MyAdminView(BaseView):
    @expose('/')
    def index(self):
        return self.render('authenticated-admin.html')

    def is_accessible(self):
        # 判断是否登陆，没有登陆的话返回403
        return current_user.is_authenticated


@app.route('/')
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'


@app.route('/login/')
def login_view():
    user = User.query.filter_by(name=USERNAME).first()
    login_user(user)
    return redirect(url_for('admin.index'))


@app.route('/logout/')
def logout_view():
    logout_user()
    return redirect(url_for('admin.index'))


admin = Admin(app, name='web_develop', template_mode='bootstrap3')

admin.add_view(ModelView(User, db.session)) # 这样子默认生成的子路径为/admin/user,可以使用endpoint='new_user',这严重路线自定义为/admin/new_user

path = os.path.join(os.path.dirname(__file__), './static')
admin.add_view(FileAdmin(path, '/static/', name='Static Files'))

# 创建一个名为Authenticated的链接，必须登陆才可以访问
admin.add_view(MyAdminView(name='Authenticated'))

# 会创建叫做Links的下拉菜单
admin.add_link(MenuLink(name='Back Home', url='/'))
admin.add_link(NotAuthenticatedMenuLink(name='Login',
                                        endpoint='login_view'))
admin.add_link(MenuLink(name='Google', category='Links',
                        url='http://www.google.com/'))
admin.add_link(MenuLink(name='Github', category='Links',
                        url='https://github.com/dongweiming'))
admin.add_link(AuthenticatedMenuLink(name='Logout',
                                     endpoint='logout_view'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)