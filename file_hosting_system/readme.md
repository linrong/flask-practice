## flask文件托管系统

### 数据库操作
```
数据库已经内置在ubuntu1.1版本

# 把添加了mysql的容器提交成为一个镜像之后，在新的镜像上实例容器并启动mysql失败，数据库因为hostname的主机名修改了，所以要做一些修改
# 不正确的做法
# 以下是删除datadir重新初始化，但会把root和默认用户也删除了
# https://blog.csdn.net/Kohang/article/details/80076570?utm_source=blogxgwz3
# https://www.cnblogs.com/yuluoluo/p/9637518.html
cd /var/lib/mysql
rm -rf *
mysqld --initialize --user=mysql --basedir=/usr --datadir=/var/lib/mysql

# 正确的做法
sudo chown -R mysql:mysql /var/lib/mysql /var/run/mysqld
# 数据库导入数据
sudo service mysql start
mysql -udgbuaa -p < ./databases/schema.sql
```

### 数据库
```
# 上面的操作是使用ubnutu docker image的，目前已经不再使用，仅做参考

# 进入数据库
docker exec -it flask_mysql_1 bash

# 数据库导入数据，账号root,密码dgbuaa
mysql -uroot -p < /home/schema.sql

# 登陆数据库
mysql -uroot -p

# 
show database;

# 
use flask;
show tables;
```

### dev操作
```
# 进入python3
docker exec -it flask_dev_1 bash

# 创建virtualenv,创建在/home目需下
virtualenv --python=python /home/virtualenv/

# 安装依赖,file_hosting_system目录下
/home/virtualenv/bin/pip install -r requirement.txt

# 启动virtualenv
source /home/virtualenv/bin/activate

# 退出virtualenv
deactivate
```