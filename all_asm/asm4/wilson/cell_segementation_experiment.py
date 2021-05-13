import diplib
import numpy as np
from diplib import PyDIPjavaio
import math

from numpy.core.multiarray import ndarray

from util.common_util import CommonUtil
from util.image_util import ImageUtil
from util.plot_util import PlotUtil
from all_asm.asm4.model.cell import Cell





if __name__ == '__main__':

    input_dir: str = CommonUtil.obtain_project_default_input_dir_path() + 'asm4/tif/'
    dir_name: str = CommonUtil.generate_date_time_str()
    output_dir_path: str = CommonUtil.obtain_project_default_output_dir_path("file_output") + dir_name

    # print(output_dir_path)
    #
    # CommonUtil.press_enter_to_exit()

    image_series_name: str = "MTLn3+EGF"    #'MTLn3-ctrl'
    image_series_name_list: list = [] #, 'MTLn3-ctrl']
    for idx in range(0, 30):
        image_suffix: str = CommonUtil.format_int_to_str_length(idx, to_length=4)
        image_series_name_list.append(image_series_name + image_suffix)

    for image_series_name in image_series_name_list:
        # img_name = "MTLn3+EGF0001"
        img = ImageUtil.obtain_image(image_series_name, input_dir);    #ImageUtil.show_image_in_dip_view(img)

        threshold_img = ImageUtil.segment_image_white(img);     #ImageUtil.show_image_in_dip_view(threshold_img)
        file_name: str = image_series_name + "_threshold_img" + ".tif"
        CommonUtil.save_image_to_folder(threshold_img, output_dir_path, file_name)


    CommonUtil.press_enter_to_exit()

