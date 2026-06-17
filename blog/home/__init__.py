
from flask import Blueprint
home = Blueprint('home', __name__,template_folder='templates',static_folder='static',static_url_path='/home/static')
# Focus：无前缀的蓝图，默认访问到全局静态资源。对于想将蓝图设为根路径（/）的操作来说，卡在静态资源的访问。解决方式，添加静态资源路径前缀static_url_path

# blueprint不生效原因1： views视图没有构建，需要导入一下
from . import views