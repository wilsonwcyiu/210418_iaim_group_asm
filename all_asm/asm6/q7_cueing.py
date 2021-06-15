import dip as dip
import diplib
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
        curr_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_diplib_image(image_name, input_dir);        ImageUtil.show_image_in_dip_view(curr_img, title="original")

        threshold_value = ImageUtil.derive_threshold_value(curr_img)
        threshold_img = ImageUtil.filter_image_by_threshold_value(curr_img, threshold_value);        ImageUtil.show_image_in_dip_view(threshold_img, title="threshold")

        gray_value_in_each_layer: list = [255, 240, 225, 210, 195, 180, 165, 150, 135, 120, 105, 90, 75, 60, 45, 30]

        image_width: int = 140
        image_height: int = 160
        image_layers: int = 16

        pixel_flattened_list = ImageUtil.obtain_pixel_value_list(threshold_img)
        pixel_binary_3d = np.reshape(pixel_flattened_list, (image_layers, image_width, image_height));        #ImageUtil.show_image_in_dip_view(pixel_binary_3d, title="pixel_3d")

        pixel_grayscale_2d = np.zeros((image_width, image_height))
        for layer_idx in range(0, 16):
            for width_idx in range(image_width):
                for height_idx in range(image_height):
                    pixel_value = pixel_binary_3d[layer_idx][width_idx][height_idx]

                    has_no_foreground_pixel = (pixel_grayscale_2d[width_idx][height_idx] == 0)
                    if pixel_value == 1 and has_no_foreground_pixel:
                        pixel_grayscale_2d[width_idx][height_idx] = gray_value_in_each_layer[layer_idx]


        ImageUtil.show_image_in_dip_view(pixel_grayscale_2d, title="depth cueing")


    CommonUtil.press_enter_to_exit()