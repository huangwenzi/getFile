import os

# 文件所在位置
File_path = "./file"

# 这个类用来专门返还html
class GetHtml():

    # 获取主界面
    @staticmethod
    def get_idxen():
        # with open("html\\main_idxen.html",'r', encoding='utf-8', errors='ignore') as f:
        #     tmp_str = f.readlines()
        # return tmp_str

        # 获取路径目录下的文件名
        file_name_list = []
        for root, dirs, files in os.walk(File_path, topdown=False):
            for name in files:
                tmp_name = os.path.join(root, name)
                # 删去'./file'
                begin = len("./file")
                app_name = tmp_name[begin:]
                file_name_list.append(app_name)
        # print("目录下有文件:" + str(file_name_list))

        # 查找符合的文件
        name_list = []
        get_type = ['mp3']
        for name in file_name_list:
            for tmp_type in get_type:
                if name.find(tmp_type) != -1:
                    name_list.append(name)
                    break
        # print("符合条件的文件有:" + str(name_list))
        
        # 填充到网页
        heml_str = ""
        template = '<a href="/getFile{}" download="{}">{}</a> <br>'
        for name in name_list:
            begin = name.rfind("\\")
            file_name = name[begin + 1:]
            tmp_str = template.format(name, file_name, file_name)
            heml_str += tmp_str

        # print(heml_str)
        return heml_str