# coding=utf-8
from flask import Flask

app=Flask(__name__)
# 增加配置管理
# 单个配置的添加
# app.config['DEBUG']=True
#多个配置的添加
app.config.update(
        DEBUG=True
        )
@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__=='__main__':
    # 开启调试模式
    app.debug=True
    app.run(host='0.0.0.0',port=9001)
