from flask import Flask,jsonify
from flask.views import MethodView

app=Flask(__name__)
# 基于调度方法的视图，对于每个HTTP方法执行不同的函数，类似RESTful API
class UserAPI(MethodView):
    def get(self):
        return jsonify({
            'username':'fake',
            'avtar':'http://lorempixel.com/100/100/nature'
            })

    def post(self):
        return 'UNSUPPORTED!'

app.add_url_rule('/user',view_func=UserAPI.as_view('userview'))

if __name__=='__main__':
    app.run(host='0.0.0.0',port=9001)
