import os
import hashlib
from functools import partial

from config import UPLOAD_FOLDER
# 获得当前文件所在的路径
HERE = os.path.abspath(os.path.dirname(__file__))

# 获得文件的md5值
# hashlib提供了常见的摘要算法,如MD5，SHA1等等,摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）
def get_file_md5(f,chunk_size=8192):
    h=hashlib.md5()
    while True:
        chunk=f.read(chunk_size)
        if not chunk:
            break
        h.update(chunk)
    return h.hexdigest()

# 返回可读文件的大小
def humanize_bytes(bytesize,precision=2):
    abbrevs=(
        (1 << 50,'PB'),# 2的50次方
        (1 << 40,'TB'),
        (1 << 30,'GB'),
        (1 << 20,'MB'),
        (1 << 10,'kB'),
        (1,'bytes')
    )
    if bytesize==1:
        return '1 byte'
    for factor,suffix in abbrevs:
        if bytesize >= factor:
            break
    return '%.*f %s'%(precision,bytesize/factor,suffix)# 保留两位小数

# 根据上传文件的目录获取上传的文件路径
# partial 函数的功能就是：把一个函数的某些参数给固定住，返回一个新的函数
# 把join的两个参数固定为HERE,UPLOAD_FOLDER
get_file_path=partial(os.path.join,HERE,UPLOAD_FOLDER)
# 其他地方调用会返回HERE+UPLOAD_FOLDER+文件路径
# 如果UPLOAD_FOLDER为/file,则会返回/file(即UPLOAD_FOLDER)+文件路径，因为UPLOAD_FOLDER已经是/开头，根目录下的啦