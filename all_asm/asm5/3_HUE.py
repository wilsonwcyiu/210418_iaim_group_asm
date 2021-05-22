# (2) Compute the average hue feature all berries in the images.
import PIL
import diplib

from util.common_util import CommonUtil
from util.image_util import ImageUtil
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
#importing required libraries
from skimage.io import imread
from skimage.transform import resize
from skimage.feature import hog
from skimage import exposure
import matplotlib.pyplot as plt



if __name__ == '__main__':

    # Configure files and directories
    input_dir: str = CommonUtil.obtain_project_default_input_dir_path() + 'asm5/'
    proj_output_dir_path: str = '../../image_output/'
    img_extension: str = ""


    folder_list: list = ["1_white"] #, "2_white", "3_white", "4_white"]

    img_relative_path_list: list = []
    for folder in folder_list:
        file_list: list = CommonUtil.obtain_file_name_list(input_dir + folder + "/")[:1]
        for file in file_list:
            img_relative_path_list.append(folder + "/" + file)


    image_rgb_array_list: list = []
    for img_relative_path in img_relative_path_list:
        image_rgb_array: PIL.JpegImagePlugin.JpegImageFile = Image.open(input_dir + img_relative_path)
        print(image_rgb_array)
        print(type(image_rgb_array))
        image_rgb_array_list.append(image_rgb_array)


    # reading the image
    # img_rgb_array = ImageUtil.obtain_image_rgb_array(input_dir + img_relative_path_list[0])
    # print(type(img_rgb_array))

    img_relative_path: str = img_relative_path_list[0]
    img = ImageUtil.obtain_diplib_image(img_relative_path, input_dir)

    ImageUtil.show_image_in_dip_view(img)




    CommonUtil.press_enter_to_exit()