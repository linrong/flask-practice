#! /usr/bin/env python
# coding=utf-8
import sys
sys.path.append('../common')
from flask import Flask, render_template, request
from flask_wtf import Form
from flask_wtf.csrf import CSRFProtect
from wtforms import TextField, PasswordField
from wtforms.validators import length, Required, EqualTo

from ext import db
from users import User
'''
pip install Flask-WTF
'''

app = Flask(__name__, template_folder='./templates')
app.config.from_object('config')
CSRFProtect(app)
db.init_app(app)


class RegistrationForm(Form):
    name = TextField('Username', [length(min=4, max=25)])
    email = TextField('Email Address', [length(min=6, max=35)])
    password = PasswordField('New Password', [
        Required(), EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(name=form.name.data, email=form.email.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return 'register successed!'
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=app.debug)