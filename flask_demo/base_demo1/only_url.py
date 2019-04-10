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
# 唯一url，基于apache以及更早的HTTP服务器的主张，保证优雅且s唯一的url
# 访问结尾不带斜线的URL会重定向到带斜线的规范的url上，有助于避免搜索引擎引用同一个页面两次
@app.route('/item/1/')
def item1():
    return 'Item1'

# 访问/item/2/会提示404
@app.route('/item/2')
def item2():
    return 'Item2'

if __name__=='__main__':
    # 开启调试模式
    app.debug=True
    app.run(host='0.0.0.0',port=9001)
