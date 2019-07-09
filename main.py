
#!/usr/bin/evn python
# coding=utf-8
# 系统或三方库
from bottle import default_app, get, run, post
from bottle import static_file, request
from beaker.middleware import SessionMiddleware

# 自写模块
from control.getHtml import GetHtml
from control.getFile import GetFile

# 公司地址 http://192.168.4.65:11000/idxen
# 神舟地址 http://192.168.235.1:11000/idxen
# 公网地址 http://118.126.112.214:11000/idxen
# 域名地址 http://thiswen.cn:11000/idxen

# 设置session参数
session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 3600,
    'session.data_dir': '/tmp/sessions/simple',
    'session.auto': True
}

# # 例子
# # 只替换某个路径名
# @get('/getGame/<filename>/index')
# def getWeMemory(filename):
#     print("getGame" + filename)
#     if "." in filename:
#         print("获取文件")
#         return static_file(filename, root='./game')
#     return getHtml.getGame(filename)
# # 获取路径下文件
# @get('/getGame/<path:path>')
# def server_memory(path):
#     print("path")
#     print(path)
#     return static_file(path, root='./game')
# # 获取网站主页
# @get('/getDogFood')
# def callback():
#     return getHtml.getDogFood()


# 获取网站主页
@get('/idxen')
def callback():
    return GetHtml.get_idxen()
# 获取某个文件
@get('/getFile/<path:path>')
def callback(path):
    # print("path:" + path)
    return static_file(path, root='./file')

GetHtml.get_idxen()

# 函数主入口
if __name__ == '__main__':
    app_argv = SessionMiddleware(default_app(), session_opts)
    run(app=app_argv, host='0.0.0.0', port=11000, debug=True)

