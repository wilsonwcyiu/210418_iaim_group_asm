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
    output_dir_str: str = CommonUtil.obtain_project_default_output_dir_path() + date_time_str + "/"



    image_name_list: list = ["AxioCamIm01"]
    # , "AxioCamIm02", "AxioCamIm03"]

    for image_name in image_name_list:
        original_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_image(image_name, dir_path=input_dir_str)
        threshold_img = ImageUtil.obtain_threshold_image(original_img);             ImageUtil.show_image_in_dip_view(threshold_img, title="threshold_img")

        se_one_side_length: int = 9
        se_shape: str = "rectangular"
        se: SE = diplib.PyDIP_bin.SE(shape=se_shape, param=se_one_side_length)

        top_hat_img_dip = top_hat_img = diplib.Tophat(threshold_img, se);           CommonUtil.save_image_to_folder(top_hat_img_dip, output_dir_str, "top_hat_img_dip.tif")

        top_hat_img_code = ImageUtil.opening(threshold_img, se_one_side_length, se_shape) < threshold_img;           CommonUtil.save_image_to_folder(top_hat_img_code, output_dir_str, "top_hat_img_code.tif")






    # top_hat_img: diplib.PyDIP_bin.Image = ImageUtil.opening(threshold_img, se_one_side_length, se_shape) < threshold_img




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