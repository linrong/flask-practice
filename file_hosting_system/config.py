DEBUG=True
# SQLAlchmy ORM框架的方式使用数据库
# dialect+driver://username:password@host:port/database，目前host使用docker-compose网络中的mysql
# dailect 数据库的实现，如MYSQL,driver是python对应的驱动，不指定则使用默认
SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:dgbuaa@mysql:3306/flask'
# 文件保存位置，要先创建
UPLOAD_FOLDER='file'
# 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它
SQLALCHEMY_TRACK_MODIFICATIONS=False