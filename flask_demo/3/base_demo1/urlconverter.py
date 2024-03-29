import urllib.parse
from flask import Flask
from werkzeug.routing import BaseConverter

app=Flask(__name__)

class ListConverter(BaseConverter):
    def __init__(self,url_map,separator="+"):
        super(ListConverter,self).__init__(url_map)
        self.separator=urllib.parse.unquote(separator)
    
    # 把路径转换成python对象
    def to_python(self,value):
        return value.split(self.separator)
   
    # 把参数转换成符合url的形式 
    def to_url(self,values):
        return self.separator.join(super(BaseConverter,self).to_url(value) for value in values)

app.url_map.converters['list']=ListConverter

@app.route('/list1/<list:page_names>/')
def list1(page_names):
    return 'Separator:{}{}'.format('+',page_names)

@app.route('/list2/<list(separator=u"|"):page_names>/')
def list2(page_names):
    return 'Separator:{}{}'.format('|',page_names)


if __name__=='__main__':
    app.run(host='0.0.0.0',port=9001)
