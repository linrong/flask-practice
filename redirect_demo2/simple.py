from flask import Flask,request,abort,redirect,url_for

app=Flask(__name__)
app.config.from_object('config')

# 请求/people时会被301跳转到/people/上，有页面永久性移走慨念
@app.route('/people/')
def people():
    name=request.args.get('name')
    if not name:
        return redirect(url_for('login'))# 默认302重定向，表示页面暂时性的转移
    user_agent = request.headers.get('User-Agent')
    return 'Name:{0};UA:{1}'.format(name,user_agent)

@app. route('/login/',methods=['GET','POST'])
def login():
    if request.method=='POST':
        user_id=request.form.get('user_id')
        return 'User:{} login'.format(user_id)
    else:
        return 'Open Login page'

@app.route('/secret/')
def secret():
    # 执行abort(401)会放弃请求并返回错误代码401，之后的代码不执行
    abort(401)
    prrint('This is never exected')

if __name__=='__main__':
    # app.debug相当于app.config['DEBUG']
    app.run(host='0.0.0.0',port=9001,debug=app.debug)
