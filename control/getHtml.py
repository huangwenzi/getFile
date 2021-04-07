import os
import control.globalData as GlobalMd 


# 获取主界面
def get_idxen():
    # 获取路径目录下的文件名
    file_name_list = []
    begin_idx = len("./file")
    for root, dirs, files in os.walk(GlobalMd.file_path, topdown=False):
        for name in files:
            tmp_name = os.path.join(root, name)
            # 删去'./file'
            app_name = tmp_name[begin_idx:]
            file_name_list.append(app_name)
    print("目录下有文件:" + str(file_name_list))

    # 查找符合的文件
    file_name_list_1 = []
    for name in file_name_list:
        can_add = True
        for tmp_type in GlobalMd.no_return_suffix:
            if name.find(tmp_type) != -1:
                can_add = False
                break
        if can_add:
            file_name_list_1.append(name)
    print("符合条件的文件有:" + str(file_name_list_1))
    
    # 填充到网页
    heml_str = ""
    template = '<a href="/getFile{}" download="{}">{}</a> <br>'
    for name in file_name_list_1:
        begin = name.rfind("\\")
        file_name = name[begin + 1:]
        tmp_str = template.format(name, file_name, file_name)
        heml_str += tmp_str

    print(heml_str)
    return heml_str