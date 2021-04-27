import diplib
import numpy as np

from diplib import PyDIPjavaio
from matplotlib import pyplot

from util.common_util import CommonUtil
from util.image_util import ImageUtil

# test_case
if __name__ == '__main__':
    print("starting...")
    sleep_sec: int = 0

    image_name_list: list = ["AxioCamIm01", "AxioCamIm02", "AxioCamIm03"]

    input_dir_str: str = CommonUtil.obtain_project_default_input_dir_path() + "asm3/"
    date_time_str: str = CommonUtil.generate_date_time_str()
    output_dir_str: str = CommonUtil.obtain_project_default_output_dir_path() + date_time_str


    original_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_image("AxioCamIm01", input_dir_str);   ImageUtil.show_image_in_dip_view(original_img, title="original img")

    filter_img = diplib.Gauss(original_img);            ImageUtil.show_image_in_dip_view(original_img, title="filter_img = diplib.Gauss(original_img")
    OD_threadhold0, threadhold1 = diplib.Threshold(filter_img);

    ImageUtil.show_image_in_dip_view(OD_threadhold0, title="OD_threadhold0 Threshold(filter_img")
    ImageUtil.show_image_in_dip_view(threadhold1, title="threadhold1 Threshold(filter_img")





    original_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_image("rect1");   ImageUtil.show_image_in_dip_view(original_img, title="original img")
    filter_img = diplib.Gauss(original_img)
    threshold_img = ImageUtil.threshold(filter_img)

    ImageUtil.show_image_in_dip_view(threshold_img, title="rect1 threshold_img Threshold(filter_img")

    print("end")

    input("Press enter to end the process...")