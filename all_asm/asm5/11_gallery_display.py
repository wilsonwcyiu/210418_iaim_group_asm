# (1) Make a gallery display out of your Group#-A dataset; this is to show the variation, so a subset will suffice.
from util.common_util import CommonUtil
from util.image_util import ImageUtil
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

if __name__ == '__main__':

    # Configure files and directories
    input_dir: str = CommonUtil.obtain_project_default_input_dir_path() + 'asm5/'
    proj_dir_path: str = '../../image_output/'
    img_extension: str = ""


    folder_list: list = ["1_black", "2_black", "3_black", "4_black"]
    pic_in_each_category: int = 8

    img_relative_path_list: list = []
    for folder in folder_list:
        file_list: list = CommonUtil.obtain_file_name_list(input_dir + folder + "/")[:pic_in_each_category]
        for file in file_list:
            img_relative_path_list.append(folder + "/" + file)


    image_rgb_array_list: list = []
    for img_relative_path in img_relative_path_list:
        image_rgb_array: np.ndarray = Image.open(input_dir + img_relative_path)
        image_rgb_array_list.append(image_rgb_array)


    total_row: int = 4;    total_col: int = pic_in_each_category
    size_tuple: tuple = (16, 8)
    plot = ImageUtil.create_multi_img_plot(image_rgb_array_list, total_row, total_col, size_tuple)
    plot.show()
