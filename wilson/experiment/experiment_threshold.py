import os

import diplib
import numpy as np

from diplib import PyDIPjavaio
from diplib.PyDIP_bin import SE
from matplotlib import pyplot

from util.common_util import CommonUtil
from util.image_util import ImageUtil




@staticmethod
def obtain_threshold_image_trial(img: PyDIPjavaio.ImageRead):
    threshold_img: diplib.PyDIP_bin.Image = None
    threshold_value: float = None
    threshold_img = diplib.Threshold(img)[0]

    return threshold_img



# test_case
if __name__ == '__main__':
    print("starting...")
    sleep_sec: int = 0

    image_name_list: list = ["AxioCamIm01", "AxioCamIm02", "AxioCamIm03"]

    input_dir_str: str = CommonUtil.obtain_project_default_input_dir_path() + "asm3/"

    date_time_str: str = CommonUtil.generate_date_time_str()
    output_dir_str: str = CommonUtil.obtain_project_default_output_dir_path() + date_time_str + "_" + os.path.basename(__file__) + "/"



    image_name_list: list = ["AxioCamIm01"]

    # , "AxioCamIm02", "AxioCamIm03"]
    # original_img1: PyDIPjavaio.ImageRead = ImageUtil.obtain_image("AxioCamIm02", dir_path=input_dir_str);
    # t1 = ImageUtil.obtain_threshold_image(original_img1)
    for image_name in image_name_list:
        original_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_image(image_name, dir_path=input_dir_str);        #ImageUtil.show_image_in_dip_view(original_img, title="original_img")
        median_filter = ImageUtil.median_filter(original_img, "rectangular");                                    #ImageUtil.show_image_in_dip_view(median_filter, title="median_filter")


        threshold_img = ImageUtil.obtain_threshold_image(median_filter);                                         ImageUtil.show_image_in_dip_view(threshold_img, title="threshold_img")


        white_img = ImageUtil.dilation(threshold_img, 10000, "rectangular");                                         ImageUtil.show_image_in_dip_view(white_img, title="white_img")
        black_img = ImageUtil.erosion(threshold_img, 10000, "rectangular");                                         ImageUtil.show_image_in_dip_view(black_img, title="black_img")

        # t1 = threshold_img < threshold_img;                                         ImageUtil.show_image_in_dip_view(t1, title="threshold_img < threshold_img")
        # t2 = threshold_img > threshold_img;                                         ImageUtil.show_image_in_dip_view(t2, title="threshold_img > threshold_img")


        # test1 = threshold_img < white_img;                                         ImageUtil.show_image_in_dip_view(test1, title="threshold_img < white_img")
        # test2 = threshold_img < black_img;                                         ImageUtil.show_image_in_dip_view(test2, title="threshold_img < black_img")
        # expect_black_img = ImageUtil.subtraction_img1_minus_img2(threshold_img, white_img);                                         ImageUtil.show_image_in_dip_view(expect_black_img, title="expect_black_img")
        # expect_original_threshold_img = ImageUtil.subtraction_img1_minus_img2(threshold_img, black_img);                                         ImageUtil.show_image_in_dip_view(expect_original_threshold_img, title="expect_original_threshold_img")


        # expect_black_img = threshold_img > white_img;                                         ImageUtil.show_image_in_dip_view(expect_black_img, title="expect_black_img")
        # expect_original_threshold_img = threshold_img > black_img;                                         ImageUtil.show_image_in_dip_view(expect_original_threshold_img, title="expect_original_threshold_img")




        # black_hat_img_dip = black_hat_img = ImageUtil.black_hat(threshold_img, se_one_side_length, se_shape);           CommonUtil.save_image_to_folder(black_hat_img_dip, output_dir_str, "black_hat_img_dip.tif")

        # black_hat_img_code = ImageUtil.opening(threshold_img, se_one_side_length, se_shape) < threshold_img;           CommonUtil.save_image_to_folder(black_hat_img_code, output_dir_str, "black_hat_img_code.tif")






    # black_hat_img: diplib.PyDIP_bin.Image = ImageUtil.opening(threshold_img, se_one_side_length, se_shape) < threshold_img




    #
    #
    # original_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_image("AxioCamIm01", input_dir_str);   ImageUtil.show_image_in_dip_view(original_img, title="original img")
    #
    # filter_img = diplib.Gauss(original_img);            ImageUtil.show_image_in_dip_view(original_img, title="filter_img = diplib.Gauss(original_img")
    # OD_threadhold0, threadhold1 = diplib.Threshold(filter_img);
    #
    # ImageUtil.show_image_in_dip_view(OD_threadhold0, title="OD_threadhold0 Threshold(filter_img")
    # ImageUtil.show_image_in_dip_view(threadhold1, title="threadhold1 Threshold(filter_img")
    #
    #
    #
    #
    #
    # original_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_image("rect1");   ImageUtil.show_image_in_dip_view(original_img, title="original img")
    # filter_img = diplib.Gauss(original_img)
    # threshold_img = ImageUtil.derive_threshold_value(filter_img)
    #
    # ImageUtil.show_image_in_dip_view(threshold_img, title="rect1 threshold_img Threshold(filter_img")

    print("end")

    input("Press enter to end the process...")