#! /usr/bin/env python
# coding=utf-8
import sys
sys.path.append('../common')
from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from ext import db
'''
pip install flask-migrate
pip install flask-script
# 
python app_migrate.py db init
python app_migrate.py db migrate
python app_migrate.py db upgrade
# 回退
python app_migrate.py db downgrade
'''
app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)

import users  # noqa

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()