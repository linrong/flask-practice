DEBUG = False

try:
    # local_settings文件是可选存在的，不进入版本库，这是常用的通过本地配置文件重载版本库配置的方式
    from local_settings import *
except ImportError:
    pass
