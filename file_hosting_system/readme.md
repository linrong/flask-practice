## flask文件托管系统

## Tip
```
root:root
python:python
# mysql
root:root@mysql
dgbuaa:dgbuaa@123.cn
```

### 创建virtualenv
```
# file_hosting_system目录下
virtualenv --python=python ./virtualenv/

# 安装依赖
sudo apt-get install libjpeg8-dev -yq
./virtualenv/bin/pip install -r requirement.txt
```
### 数据库操作
```
# 不正确的做法
# 以下是删除datadir重新初始化，但会把root和默认用户也删除了
# 数据库因为hostname的主机名修改了，所以要做一些修改
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
