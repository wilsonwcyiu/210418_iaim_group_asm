# Compute the HOG feature vector for all of your images and store these in one comma separated file – for cell sizes use 16 and 64, resulting in two sets.
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


# https://www.thepythoncode.com/article/hog-feature-extraction-in-python
# https://www.analyticsvidhya.com/blog/2019/09/feature-engineering-images-introduction-hog-feature-descriptor/
# https://lilianweng.github.io/lil-log/2017/10/29/object-recognition-for-dummies-part-1.html
if __name__ == '__main__':

    # Configure files and directories
    input_dir: str = CommonUtil.obtain_project_default_input_dir_path() + 'asm5/'
    output_dir: str = '../../file_output/' + CommonUtil.generate_date_time_str() + "/"
    img_extension: str = ""


    folder_list: list = ["1_white", "2_white", "3_white", "4_white"]

    img_relative_path_list: list = []
    for folder in folder_list:
        file_list: list = CommonUtil.obtain_file_name_list(input_dir + folder + "/")#[:2]
        for file in file_list:
            img_relative_path_list.append(folder + "/" + file)


    # image_rgb_array_list: list = []
    # for img_relative_path in img_relative_path_list:
    #     image_rgb_array: PIL.JpegImagePlugin.JpegImageFile = Image.open(input_dir + img_relative_path)
    #     image_rgb_array_list.append(image_rgb_array)


    img_resize_dimention_tuple: tuple = (128*4, 64*4)

    hog_data_list: list = []
    for img_relative_path in img_relative_path_list:
        print("img_relative_path: ", img_relative_path)

        img_rgb_array = ImageUtil.obtain_image_rgb_array(input_dir + img_relative_path);     #print(type(img_rgb_array)); ImageUtil.show_image_in_dip_view(img_rgb_array)

        resized_img = resize(img_rgb_array, img_resize_dimention_tuple)

        fd_hog_desc_list, hog_image_rgb_array = hog(resized_img, orientations=9,
                                                    pixels_per_cell=(4, 4), cells_per_block=(1, 1),
                                                    visualize=True, multichannel=True)

        fd_hog_desc_str_list = [str(float) for float in fd_hog_desc_list]
        fd_hog_desc_str_list = CommonUtil.insert_to_list(fd_hog_desc_str_list, 0, img_relative_path)

        hog_data_list.append(tuple(fd_hog_desc_str_list))

    # CommonUtil.make_dir(output_dir)
    CommonUtil.write_csv_file(hog_data_list, output_dir, "hog_16_all_while_img.csv")





    hog_data_list: list = []
    for img_relative_path in img_relative_path_list:
        print("img_relative_path: ", img_relative_path)

        img_rgb_array = ImageUtil.obtain_image_rgb_array(input_dir + img_relative_path);     #print(type(img_rgb_array)); ImageUtil.show_image_in_dip_view(img_rgb_array)

        resized_img = resize(img_rgb_array, img_resize_dimention_tuple)

        fd_hog_desc_list, hog_image_rgb_array = hog(resized_img, orientations=9,
                                                    pixels_per_cell=(8, 8), cells_per_block=(1, 1),
                                                    visualize=True, multichannel=True)

        fd_hog_desc_str_list = [str(float) for float in fd_hog_desc_list]
        fd_hog_desc_str_list = CommonUtil.insert_to_list(fd_hog_desc_str_list, 0, img_relative_path)

        hog_data_list.append(tuple(fd_hog_desc_str_list))

    # CommonUtil.make_dir(output_dir)
    CommonUtil.write_csv_file(hog_data_list, output_dir, "hog_64_all_while_img.csv")

    # print(fd_hog_desc_list.size)
    # print(type(fd_hog_desc_list))
    # ImageUtil.show_image_in_dip_view(hog_image_rgb_array)
    # plt.show()
    CommonUtil.press_enter_to_exit()