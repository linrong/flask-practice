from flask import Flask,jsonify,render_template,make_response
from werkzeug.wrappers import Response

app=Flask(__name__)
# 目前对于这个的使用还不是很了解，返回元组的时候如果不调用这个会报404错误，即下面的两个d方
class JSONResponse(Response):
    @classmethod
    def force_type(cls,rv,environ=None):
        if isinstance(rv,dict):
            rv=jsonify(rv)
        return super(JSONResponse,cls).force_type(rv,environ)

app.response_class=JSONResponse

@app.route('/')
def hello_world():
    return {'message':'Hello World!'}

@app.route('/custom_headers')
def headers():
    return {'headers':[1,2,3]},201,[('X-Request-Id','100')]
# render_template用于渲染模板，默认使用Jinja2的模板引擎
#@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'),404

# 使用make_response可以使模板更加灵活，可以添加一些额外的工作，比如设置cookie,头信息等
@app.errorhandler(404)
def not_found(error):
    resp=make_response(render_template('error.html'),404)
    return resp


if __name__=='__main__':
    app.run(host='0.0.0.0',port=9001)
