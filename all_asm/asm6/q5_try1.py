import dip as dip
import diplib
import numpy
from diplib import PyDIPjavaio

from util.common_util import CommonUtil
from util.image_util import ImageUtil
from util.plot_util import PlotUtil
import numpy as np


if __name__ == '__main__':

    # Configure files and directories
    input_dir: str = CommonUtil.obtain_project_default_input_dir_path() + 'asm6/'
    proj_output_dir_path: str = CommonUtil.obtain_project_default_output_dir_path() + CommonUtil.generate_date_time_str() + "/"

    image_name_list: list = ["CHROMO3D.ics"]

    for image_name in image_name_list:
        curr_img: diplib.PyDIP_bin.Image = ImageUtil.obtain_diplib_image(image_name, input_dir);        ImageUtil.show_image_in_dip_view(curr_img, title="original image")


        # https://qiftp.tudelft.nl/dipref/Rotation3d.html
        x_rotation_angle_radius: float = 0.0
        y_rotation_angle_radius: float = 0.0
        z_rotation_angle_radius: float = 0.0

        for idx in range(63):
            x_rotation_angle_radius += 0.1
            # y_rotation_angle_radius += 0.1
            # z_rotation_angle_radius += 0.1
            rotate_img = diplib.Rotation3D(curr_img,
                                           x_rotation_angle_radius,
                                           y_rotation_angle_radius,
                                           z_rotation_angle_radius)

            ImageUtil.show_image_in_dip_view(rotate_img, title="rotate_img_" + str(idx), position_tuple=(300,100))






    CommonUtil.press_enter_to_exit()