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
pip install uwsgi
启动uwsgi
uwsgi --http 0.0.0.0:8080 --wsgi-file app.py --callable app --process 4 --threads 2 --stats 0.0.0.0:8081

--http-socket和--http两个不同的选项，使用nginx时应该使用--http-socket
合理的进程和线程不是简单的计算可以得出的，可以使用uwsgitop测试，使用--stats参数，得出比较好的配置
'''