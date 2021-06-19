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

    image_width: int = 512
    image_height: int = 512
    image_layers: int = 8

    # image_name_list: list = ["convollaria_512_10X_sameTracks_green.ics"]
    # image_name_list: list = ["convollaria_512_10X_sameTracks_green_red.ics"]
    image_name_list: list = ["convollaria_512_10X_twoTracks_green_red.ics"]

    gray_value_in_each_layer: list = [255, 240, 225, 210, 195, 180, 165, 150, 135, 120, 105, 90, 75, 60, 45, 30]

    pixel_for_each_color: int = image_width * image_height * image_layers;          print("pixel_for_each_color", pixel_for_each_color)
    for image_name in image_name_list:
        curr_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_diplib_image(image_name, input_dir);        ImageUtil.show_image_in_dip_view(curr_img, title="original")

        threshold_value = ImageUtil.derive_threshold_value(curr_img)
        threshold_img = ImageUtil.filter_image_by_threshold_value(curr_img, threshold_value);        ImageUtil.show_image_in_dip_view(threshold_img, title="threshold")

        pixel_flattened_list: list = ImageUtil.obtain_pixel_value_list(threshold_img);             print("pixel_flattened_list", len(pixel_flattened_list))
        green_pixel_flattened_list = pixel_flattened_list[: pixel_for_each_color];                 print(len(green_pixel_flattened_list))
        pixel_binary_3d = np.reshape(green_pixel_flattened_list, (image_layers, image_width, image_height));        #ImageUtil.show_image_in_dip_view(pixel_binary_3d, title="pixel_3d")

        pixel_grayscale_2d = np.zeros((image_width, image_height))
        for layer_idx in range(0, image_layers):
            for width_idx in range(image_width):
                for height_idx in range(image_height):
                    pixel_value = pixel_binary_3d[layer_idx][width_idx][height_idx]

                    has_no_foreground_pixel = (pixel_grayscale_2d[width_idx][height_idx] == 0)
                    if pixel_value == 1 and has_no_foreground_pixel:
                        pixel_grayscale_2d[width_idx][height_idx] = gray_value_in_each_layer[layer_idx]


        ImageUtil.show_image_in_dip_view(pixel_grayscale_2d, title="depth cueing")

        # file_name: str = "q11_depth_cueing_sameTracks_green.png"
        # file_name: str = "q11_depth_cueing_sameTracks_green_red.png"
        file_name: str = "q11_depth_cueing_twoTracks_green_red.png"
        CommonUtil.save_ndarray_as_image(pixel_grayscale_2d, proj_output_dir_path, file_name)

    CommonUtil.press_enter_to_exit()