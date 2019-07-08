from bottle import static_file


# 这个类用来专门返还文件
class GetFile():

    # 校验权限
    @staticmethod
    def check_user(data):
        user = data["user"]
        password = data["password"]
        if user[0] != "qwe" or password[0] != "123":
            return False
        
        return True

    # 获取某个文件
    @staticmethod
    def get_file(data):
        # 先检查权限
        if not GetFile.check_user(data):
            return False
        
        # # 返回文本
        # # 只返回文本的内容
        # return static_file("1.txt", root='./file')

        # # 返回对象
        # # 
        # return {"a": "a", "b": 1}

        # 返回音频
        # 
        return static_file("2.mp3", root='./file')

