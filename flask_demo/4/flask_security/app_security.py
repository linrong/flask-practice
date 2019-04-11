#! /usr/bin/env python
# coding=utf-8
import sys
sys.path.append('../common')
from functools import wraps, reduce
from operator import or_

from flask import Flask, abort
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user
from flask_security import (Security, SQLAlchemyUserDatastore,
                            UserMixin, RoleMixin, login_required)
from flask_security.forms import LoginForm


app = Flask(__name__, template_folder='./templates')
app.config.from_object('config')
app.config['SECURITY_LOGIN_USER_TEMPLATE'] = 'login_user.html'  # 指定flask_security指定对应的变量替换模板
app.config['SECURITY_PASSWORD_SALT'] = 'salt'

db = SQLAlchemy(app)
'''
pip install flask-security
pip install bcrypt # 密码加密方式
'''

class Permission(object):
    LOGIN = 0x01
    EDITOR = 0x02
    OPERATOR = 0x04
    ADMINISTER = 0xff
    PERMISSION_MAP = {
        LOGIN: ('login', 'Login user'),
        EDITOR: ('editor', 'Editor'),
        OPERATOR: ('op', 'Operator'),
        ADMINISTER: ('admin', 'Super administrator')# 使用oxff最大值，表示拥有最大权限
    }
# 用户和角色多对多，使用辅助表
roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer,
              db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id')))

# 定义角色模式
class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    permissions = db.Column(db.Integer, default=Permission.LOGIN)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))# 添加roles字段，指向模型Role
                            # backref表示反向引用
    # 增加权限判断方法
    def can(self, permissions):
        if self.roles is None:
            return False
        all_perms = reduce(or_, map(lambda x: x.permissions, self.roles))
        return all_perms & permissions == permissions

    def can_admin(self):
        return self.can(Permission.ADMINISTER)


user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore, register_form=LoginForm)


@security.login_context_processor # 登陆时视图会触发
def security_login_processor():
    print('Login')
    return {}

# 添加访问验证装饰器
def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def _deco(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)
        return _deco
    return decorator


def admin_required(f):
    return permission_required(Permission.ADMINISTER)(f)


@app.before_first_request
def create_user():
    db.drop_all()
    db.create_all()

    for permissions, (name, desc) in Permission.PERMISSION_MAP.items():# 角色表新增数据
        user_datastore.find_or_create_role(
            name=name, description=desc, permissions=permissions)
    for email, passwd, permissions in (
            ('test', 'test', (
                Permission.LOGIN, Permission.EDITOR)),
            ('admin', 'admin', (Permission.ADMINISTER,))):# 用户表新增数据
        user_datastore.create_user(email=email, password=passwd)
        for permission in permissions:
            user_datastore.add_role_to_user(
                email, Permission.PERMISSION_MAP[permission][0])
    db.session.commit()


@app.route('/')
@login_required # 判断是否登陆，没有则跳转登陆页面
@permission_required(Permission.LOGIN)
def index():
    return 'Login in'


@app.route('/admin/')
@login_required
@admin_required
def admin():
    return 'Only administrators can see this!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=app.debug)