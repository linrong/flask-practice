#! /usr/bin/env python
# coding=utf-8
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

'''
pip install gunicorn
启动gunicorn
gunicorn --workers=3 app:app -b 0.0.0.0:8080
第一个app是模块名字，第二个是文件中Flask实例的名字
workers数量推荐为CPU的个数*2+1
获取CPU个数:
python -c 'import multiprocessing;print(multiprocessing.cpu_count())'
'''