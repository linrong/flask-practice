# coding=utf-8
from flask import Flask

app=Flask(__name__)
# 增加配置管理
app.config['DEBUG']=True

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__=='__main__':
    app.run(host='0.0.0.0',port=9001)
