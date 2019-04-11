#! /usr/bin/env python
# coding=utf-8
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
'''
# flask调试，开启debug下会在浏览器查看环境变量，上下文内容等
pip install flask-debugtoolbar
'''
app = Flask(__name__)

app.debug = True

app.config['SECRET_KEY'] = 'a secret key'

toolbar = DebugToolbarExtension(app)


@app.route('/')
def hello():
    return '<body></body>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=app.debug)
