#coding=utf-8

from Config import global_parameter


# 截图放到report下的img目录下
def get_img(dr, filename):
    path = global_parameter.img_path + '\\' + filename
    dr.get_screen_shot(path)