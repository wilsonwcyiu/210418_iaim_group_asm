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
    img_rgb_array = ImageUtil.obtain_image_rgb_array(input_dir + img_relative_path_list[0])
    print(type(img_rgb_array))

    ImageUtil.show_image_in_dip_view(img_rgb_array)


    plt.axis("off")
    plt.imshow(img_rgb_array)
    print(img_rgb_array.shape)

    # resizing image
    resized_img = resize(img_rgb_array, (128 * 4, 64 * 4))
    plt.axis("off")
    plt.imshow(resized_img)
    print(resized_img.shape)


    #creating hog features
    fd_hog_desc_list, hog_image_rgb_array = hog(resized_img, orientations=9,
                                                pixels_per_cell=(8, 8), cells_per_block=(1, 1),
                                                visualize=True, multichannel=True)


    CommonUtil.make_dir(output_dir)
    CommonUtil.write_csv_file([fd_hog_desc_list], output_dir, "test1.csv")

    print(fd_hog_desc_list.size)
    print(type(fd_hog_desc_list))

    # print(type(hog_image_rgb_array))
    ImageUtil.show_image_in_dip_view(hog_image_rgb_array)

    # plt.axis("off")
    # plt.imshow(hog_image, cmap="gray")

    # plt.show()
    CommonUtil.press_enter_to_exit()