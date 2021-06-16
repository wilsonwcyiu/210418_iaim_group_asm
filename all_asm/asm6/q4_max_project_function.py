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


        image_width: int = 140
        image_height: int = 160
        image_layers: int = 16


        # Max projection from original image
        pixel_list = ImageUtil.obtain_pixel_value_list(curr_img)
        pixel_3d = np.reshape(pixel_list, (image_layers, image_width, image_height));

        # print(type(pixel_3d), pixel_3d.shape)

        max_projection_list = np.zeros((image_width, image_height))
        for layer_idx in range(16):
            for width_idx in range(image_width):
                for height_idx in range(image_height):
                    pixel_value = pixel_3d[layer_idx][width_idx][height_idx]

                    if pixel_value > max_projection_list[width_idx][height_idx]:
                        max_projection_list[width_idx][height_idx] = pixel_value

        ImageUtil.show_image_in_dip_view(max_projection_list, title="Max projection from original image")
        file_name: str = "max_projection_original_img.png"
        CommonUtil.save_ndarray_as_image(max_projection_list, proj_output_dir_path, file_name)





        # Max projection from threshold image
        threshold_img = ImageUtil.segment_image_white(curr_img)
        pixel_list = ImageUtil.obtain_pixel_value_list(threshold_img)
        pixel_3d = np.reshape(pixel_list, (image_layers, image_width, image_height));

        max_projection_list = np.zeros((image_width, image_height))
        for layer_idx in range(16):
            for width_idx in range(image_width):
                for height_idx in range(image_height):
                    pixel_value = pixel_3d[layer_idx][width_idx][height_idx]

                    if pixel_value > max_projection_list[width_idx][height_idx]:
                        max_projection_list[width_idx][height_idx] = pixel_value

        ImageUtil.show_image_in_dip_view(max_projection_list, title="Max projection from binary image")
        file_name: str = "max_projection_binary_img.png"
        CommonUtil.save_ndarray_as_image(max_projection_list, proj_output_dir_path, file_name)



    CommonUtil.press_enter_to_exit()