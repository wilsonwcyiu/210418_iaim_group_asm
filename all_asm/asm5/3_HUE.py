# (2) Compute the average hue feature all berries in the images.
import PIL
import diplib
from diplib import PyDIPjavaio

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

from skimage import data
import matplotlib.pyplot as plt

from util.plot_util import PlotUtil


# https://www.programmersought.com/article/54406295171/
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
        # print(image_rgb_array)
        # print(type(image_rgb_array))
        image_rgb_array_list.append(image_rgb_array)


    # reading the image
    # img_rgb_array = ImageUtil.obtain_image_rgb_array(input_dir + img_relative_path_list[0])
    # print(type(img_rgb_array))

    # img_relative_path: str = img_relative_path_list[0]
    img_path = "1_white/1.j_Mulberry_1.jpg"
    # img_path = "../asm4/tif/MTLn3+EGF0000.tif"

    img: diplib.ImageRead = ImageUtil.obtain_diplib_image(img_path, input_dir);    ImageUtil.show_image_in_dip_view(img)



    # print(img.ColorSpace())

    gray_scale_img = ImageUtil.convert_to_gray_scale(img);      ImageUtil.show_image_in_dip_view(gray_scale_img)
    contrasted_img = diplib.ContrastStretch(gray_scale_img);    #ImageUtil.show_image_in_dip_view(contrasted_img)

    se_one_side_length = 50;    se_shape="elliptic"
    o = ImageUtil.opening(contrasted_img, se_one_side_length, se_shape);        #ImageUtil.show_image_in_dip_view(o)


    black_top_hat = ImageUtil.black_hat(contrasted_img, se_one_side_length, se_shape);      #ImageUtil.show_image_in_dip_view(black_top_hat)
    # pix_list = ImageUtil.obtain_pixel_value_list(black_top_hat)
    # p = PlotUtil.create_histogram_plot(pix_list)
    # p.show()

    segment_img = ImageUtil.segment_image_white(black_top_hat);      ImageUtil.show_image_in_dip_view(segment_img)

    ws_img = diplib.Watershed(contrasted_img, segment_img, connectivity=2, flags={"binary", "high first"});      ImageUtil.show_image_in_dip_view(ws_img)
    # ImageUtil.watershed(contrasted_img, segment_img)






    segmentation_pixel_list = ImageUtil.obtain_pixel_value_list(segment_img)
    img_rgb_tuple_list: list = ImageUtil.obtain_rgb_tuple_list(img)

    # print(segmentation_pixel_list)

    burries_rgb_tuple_list: list = []
    for i in range(len(segmentation_pixel_list)):
        if segmentation_pixel_list[i] == True:
            burries_rgb_tuple_list.append(img_rgb_tuple_list[i])


    # image = data.imread( input_dir + img_path)
    pixel_list = ImageUtil.obtain_rgb_tuple_list_list(img)
    avg_hue_value: float = ImageUtil.avg_hue_value(pixel_list)

    print("avg_hue_value", avg_hue_value)








    # histogram = ImageUtil.obtain_pixel_value_list(contrasted_img)
    # plot = PlotUtil.create_histogram_plot(histogram, plot_id=2, bins=256)
    # plot.show()
    #
    #
    # histogram = ImageUtil.obtain_pixel_value_list(gray_scale_img)
    # plot = PlotUtil.create_histogram_plot(histogram, plot_id=1, bins=256)
    # plot.show()


    CommonUtil.press_enter_to_exit()



    # ImageUtil.obtain_histogram_list

    CommonUtil.press_enter_to_continue()

    blackhat_img = ImageUtil.black_hat(gray_scale_img, se_one_side_length=60, se_shape="elliptic");    ImageUtil.show_image_in_dip_view(blackhat_img, title="blackhat_img")


    CommonUtil.press_enter_to_continue()




    # se_one_side_length: int = 10;   se_shape: str = "elliptic"
    # opening_img = ImageUtil.opening(gray_scale_img, se_one_side_length, se_shape);    ImageUtil.show_image_in_dip_view(opening_img)


    # eros_img = ImageUtil.threshold(gray_scale_img, se_one_side_length=10, se_shape="parabolic");          ImageUtil.show_image_in_dip_view(eros_img)
    threashold_img = ImageUtil.segment_image_white(blackhat_img);          ImageUtil.show_image_in_dip_view(threashold_img, title="threashold_img")

    watershed_img = ImageUtil.watershed(gray_scale_img, threashold_img);     ImageUtil.show_image_in_dip_view(watershed_img)

    CommonUtil.press_enter_to_exit()





    CommonUtil.press_enter_to_exit()