from flask import Flask,url_for

app=Flask(__name__)

@app.route('/')
def index():
    pass

@app.route('/login')
def login():
    pass

@app.route('/user/<username>')
def profile(username):
    pass

with app.test_request_context():
    print (url_for('index'))
    print (url_for('login'))
    print (url_for('login',next='/'))
    print (url_for('profile',username='John Doe'))

# 运行结果
# /
# /login
# /login?next=/
# /user/John%20Doe

# 使用url_for构造URL，接受函数名作为第一个参数，也接受对应的URL规则的变量部分的命名参数，未知变量部分会添加到URL末尾作为查询参数
# 相当于在模板中硬编码的优点：
# 1.反向构建比硬编码的描述性更好，可以一次性修改URL，而不用到处寻找修改
# 2.URL构建会转义特殊字符和Unicode数据，不需要我们去处理
# 3.自行解决应用不做URL的根目录下，比如在/myapplication下，而不在下
