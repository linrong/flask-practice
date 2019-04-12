##### hello
* 最小的应用
```bash
# 安装Flask
pip install Flask

# code
# coding=utf-8
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
# python hello.py 运行
# app.run一般只用于调试，生产环境使用uwsgi或者gunicorn
```

* 配置管理
```bash
# 1.
app = Flask(__name__)
app.config['DEBUG']=True
# 2.
app.config.update(
    DEBUG=True,
    ...
)
# 3.多配置通过文件的管理,创建settings.py文件
# 3.1 通过配置文件加载
app.config.from_object('settings')# 通过字符串的模块名字
或者通过引用之后使用模块对象
import settings
app.config.from_object(settings)
# 3.2通过文件名字加载，不限于.py后缀的文件名
app.config.from_pyfile('settings.py',silent=True)# 默认当文件不存在时，会抛出异常。使用silent=True时不会抛出异常，只会返回False
# 3.3通过环境变量加载
export YOURAPPLICATION_SETTINGS='settings.py'
app.config.from_envvar('YOURAPPLICATION_SETTINGS')
```