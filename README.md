# flask
This repository is mainly about some thoughts and demo in my study of flask

# python3:1.0
* [python3:1.0](https://github.com/linrong/dev_tools/tree/master/docker/python)

* [dockerhub](https://cloud.docker.com/repository/docker/linrong/python3)
* [flask](https://dormousehole.readthedocs.io/en/latest/)
# use with linrong/python3:1.0
docker-compose up -d

### virtualenvwrapper
```
# 进入python3
docker exec -it flask_dev_1 bash


# 使用virtualenvwrapper管理虚拟环境
# 创建目录
mkdir /home/virtualenv
# 初始化
export WORKON_HOME=/home/virtualenv
source /usr/local/bin/virtualenvwrapper.sh

# 创建虚拟环境
mkvirtualenv flask
# 查看当前拥有虚拟环境
workon
# 进行虚拟环境,也可以直接切换虚拟环境
workon flask
# 退出virtualenv
deactivate

# 列出所有虚拟环境
lsvirtualenv
# 列出单个虚拟环境信息
showvirtualenv
# 删除一个虚拟环境
rmvirtualenv
# 拷贝虚拟环境
cpvirtualenv
# 所有虚拟环境执行统一命令
all virtuallenv pip install flask
```