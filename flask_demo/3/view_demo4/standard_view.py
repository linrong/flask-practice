from flask import Flask,request,render_template
from flask.views import View
# 标准视图，灵感来源于django的基于类的通用视图方式，这样的视图可以进行继承
# 标准视图需要继承于flask.view.VIew ,必须实现dispatch_request
app=Flask(__name__,template_folder='../../templates')

class BaseView(View):
    def get_template_name(self):
        raise NotImplementedError()

    def render_template(self,context):
        return render_template(self.get_template_name(),**context)

    def dispatch_request(self):
        if request.method!='GET':
            return 'UNSUPPORTED!'

        context={'users':self.get_users()}
        return self.render_template(context)

class UserView(BaseView):

    def get_template_name(self):
        return 'chapter3/section1/users.html'

    def get_users(self):
        return[{
            'username':'fake',
            'avatar':'http://lorempixel.com/100/100/nature/'
            }]

app.add_url_rule('/users',view_func=UserView.as_view('userview'))

if __name__=='__main__':
    app.run(host='0.0.0.0',port=9001)
