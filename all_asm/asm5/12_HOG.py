# Compute the HOG feature vector for all of your images and store these in one comma separated file – for cell sizes use 16 and 64, resulting in two sets.
import PIL
import diplib
import csv

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

    # Configure files and directories and settings
    input_dir: str = CommonUtil.obtain_project_default_input_dir_path() + 'asm5/'
    proj_dir_path: str = '../../file_output/'
    img_group: str = 'black'  # white / black
    cell_size: int = 16  # 16 / 64
    feature: str = 'hog'

    types: list = ['1', '2', '3', '4']  # [number]_[black/white] - number means sage of ripening

    first_line = True
    with open(proj_dir_path + 'asm5/' + feature + '_' + img_group + '_' + str(cell_size) + '.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=",")

        for stage in types:
            file_list: list = CommonUtil.obtain_file_name_list(input_dir + stage + '_' + img_group + '/')
            for file in file_list:
                img_rgb = ImageUtil.obtain_image_rgb_array(input_dir + stage + '_' + img_group + '/' + file)
                img_gray = ImageUtil.obtain_image_gray_array(input_dir + stage + '_' + img_group + '/' + file)

                # resizing image to have same number of features for images of different size
                resized_img = resize(img_rgb, (128 * 4, 64 * 4))


                # creating hog features for resized image
                fd, hog_image = hog(resized_img, orientations=8,
                                    pixels_per_cell=(np.sqrt(cell_size), np.sqrt(cell_size)),
                                    cells_per_block=(1, 1), visualize=True, multichannel=True)

                if first_line:  # first line of a file is a header
                    header = ['Label'] + ['Feature ' + str(i) for i in range(len(fd))]
                    # for i in range(len(fd)):
                    #     header.append("Feature "+str(i))
                    writer.writerow(header)
                    first_line = False

                # fd contains the features for classification
                # inserting stage of ripening on the first position of each line,
                # which serves as label for classification
                line = np.insert(fd, 0, int(stage))

                # writing to csv file
                writer.writerow(line)



    cell_size = 64  # 16 / 64

    first_line = True
    with open(proj_dir_path + 'asm5/' + feature + '_' + img_group + '_' + str(cell_size) + '.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=",")

        for stage in types:
            file_list: list = CommonUtil.obtain_file_name_list(input_dir + stage + '_' + img_group + '/')
            for file in file_list:
                img_rgb = ImageUtil.obtain_image_rgb_array(input_dir + stage + '_' + img_group + '/' + file)
                img_gray = ImageUtil.obtain_image_gray_array(input_dir + stage + '_' + img_group + '/' + file)

                # resizing image to have same number of features for images of different size
                resized_img = resize(img_rgb, (128 * 4, 64 * 4))

                # creating hog features for resized image
                fd, hog_image = hog(resized_img, orientations=8,
                                    pixels_per_cell=(np.sqrt(cell_size), np.sqrt(cell_size)),
                                    cells_per_block=(1, 1), visualize=True, multichannel=True)

                if first_line:  # first line of a file is a header
                    header = ['Label'] + ['Feature ' + str(i) for i in range(len(fd))]
                    # for i in range(len(fd)):
                    #     header.append("Feature "+str(i))
                    writer.writerow(header)
                    first_line = False

                # fd contains the features for classification
                # inserting stage of ripening on the first position of each line,
                # which serves as label for classification
                line = np.insert(fd, 0, int(stage))

                # writing to csv file
                writer.writerow(line)


    # folder_list: list = ["1_black", "2_black", "3_black", "4_black"]
    #
    # img_relative_path_list: list = []
    # for folder in folder_list:
    #     file_list: list = CommonUtil.obtain_file_name_list(input_dir + folder + "/")#[:2]
    #     for file in file_list:
    #         img_relative_path_list.append(folder + "/" + file)
    #
    #
    # img_resize_dimention_tuple: tuple = (128*4, 64*4)
    #
    # hog_data_list: list = []
    # for img_relative_path in img_relative_path_list:
    #     print("img_relative_path: ", img_relative_path)
    #
    #     img_rgb_array = ImageUtil.obtain_image_rgb_array(input_dir + img_relative_path);     #print(type(img_rgb_array)); ImageUtil.show_image_in_dip_view(img_rgb_array)
    #
    #     resized_img = resize(img_rgb_array, img_resize_dimention_tuple)
    #
    #     fd_hog_desc_list, hog_image_rgb_array = hog(resized_img, orientations=9,
    #                                                 pixels_per_cell=(4, 4), cells_per_block=(1, 1),
    #                                                 visualize=True, multichannel=True)
    #
    #     fd_hog_desc_str_list = [str(float) for float in fd_hog_desc_list]
    #     fd_hog_desc_str_list = CommonUtil.insert_to_list(fd_hog_desc_str_list, 0, img_relative_path)
    #
    #     hog_data_list.append(tuple(fd_hog_desc_str_list))
    #
    # CommonUtil.make_dir(output_dir)
    # CommonUtil.write_csv_file(hog_data_list, output_dir, "hog_16_all_while_img.csv")
    #
    #
    #
    #
    #
    # hog_data_list: list = []
    # for img_relative_path in img_relative_path_list:
    #     print("img_relative_path: ", img_relative_path)
    #
    #     img_rgb_array = ImageUtil.obtain_image_rgb_array(input_dir + img_relative_path);     #print(type(img_rgb_array)); ImageUtil.show_image_in_dip_view(img_rgb_array)
    #
    #     resized_img = resize(img_rgb_array, img_resize_dimention_tuple)
    #
    #     fd_hog_desc_list, hog_image_rgb_array = hog(resized_img, orientations=9,
    #                                                 pixels_per_cell=(8, 8), cells_per_block=(1, 1),
    #                                                 visualize=True, multichannel=True)
    #
    #     fd_hog_desc_str_list = [str(float) for float in fd_hog_desc_list]
    #     fd_hog_desc_str_list = CommonUtil.insert_to_list(fd_hog_desc_str_list, 0, img_relative_path)
    #
    #     hog_data_list.append(tuple(fd_hog_desc_str_list))
    #
    # CommonUtil.make_dir(output_dir)
    # CommonUtil.write_csv_file(hog_data_list, output_dir, "hog_64_all_while_img.csv")
    #
    # # print(fd_hog_desc_list.size)
    # # print(type(fd_hog_desc_list))
    # # ImageUtil.show_image_in_dip_view(hog_image_rgb_array)
    # # plt.show()
    # CommonUtil.press_enter_to_exit()