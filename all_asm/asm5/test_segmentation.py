# Segmentation of berry images

import PIL
import diplib

from util.common_util import CommonUtil
from util.image_util import ImageUtil

from PIL import Image


if __name__ == '__main__':

    # Configure files and directories
    input_dir: str = CommonUtil.obtain_project_default_input_dir_path() + 'asm5/'
    proj_output_dir_path: str = '../../image_output/'
    img_extension: str = ""

    folder_list: list = ["1_white", "4_white"]

    for folder in folder_list:
        img_relative_path_list: list = []

        # ATM only first image of folder
        file_list: list = CommonUtil.obtain_file_name_list(input_dir + folder + "/")[:1]
        for file in file_list:
            img_relative_path_list.append(folder + "/" + file)

        # Go through every image


        '''
        img_rgb_array_list: list = []

        for img_relative_path in img_relative_path_list:
            img_rgb_array: PIL.JpegImagePlugin.JpegImageFile = Image.open(input_dir + img_relative_path)
            img_rgb_array_list.append(img_rgb_array)
        '''