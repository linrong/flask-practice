DEBUG=True
# SQLAlchmy ORM框架的方式使用数据库
# dialect+driver://username:password@host:port/database
# dailect 数据库的实现，如MYSQL,driver是python对应的驱动，不指定则使用默认
SQLALCHEMY_DATABASE_URI='mysql://web:web@localhost:3306/r'
# 文件保存位置，要先创建
UPLOAD_FOLDER='/home/python/flask/file'
# 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它
SQLALCHEMY_TRACK_MODIFICATIONS=False