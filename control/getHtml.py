

# 这个类用来专门返还html
class GetHtml():

    # 获取主界面
    @staticmethod
    def get_idxen():
        with open("html\\main_idxen.html",'r', encoding='utf-8', errors='ignore') as f:
            tmp_str = f.readlines()
        return tmp_str