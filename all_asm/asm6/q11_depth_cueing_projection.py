import diplib as dip
import diplib
from diplib import PyDIPjavaio

from util.common_util import CommonUtil
from util.image_util import ImageUtil

import numpy as np


def mean_proj(img_layers_list: list, image_width: int, image_height: int):
    projected_img = np.zeros((image_width, image_height))

    for width_idx in range(image_width):
        for height_idx in range(image_height):
            sum_pixel_value = 0
            for layer_idx in range(0, len(img_layers_list)):
                current_pixel_value = img_layers_list[layer_idx][width_idx][height_idx]
                sum_pixel_value += current_pixel_value
            projected_img[width_idx][height_idx] = sum_pixel_value/len(img_layers_list)

    CommonUtil.save_image_to_folder(projected_img, proj_output_dir_path, 'mean_projection.jpg')


def max_proj(img_layers_list: list, image_width: int, image_height: int):
    projected_img = np.zeros((image_width, image_height))

    for width_idx in range(image_width):
        for height_idx in range(image_height):
            max_pixel_value = 0
            for layer_idx in range(0, len(img_layers_list)):
                current_pixel_value = img_layers_list[layer_idx][width_idx][height_idx]
                if max_pixel_value < current_pixel_value:
                    max_pixel_value = current_pixel_value
            projected_img[width_idx][height_idx] = max_pixel_value

    CommonUtil.save_image_to_folder(projected_img, proj_output_dir_path, 'max_projection.jpg')


if __name__ == '__main__':
    # Configuration files and directories
    input_dir: str = CommonUtil.obtain_project_default_input_dir_path() + 'asm6/'
    proj_output_dir_path: str = CommonUtil.obtain_project_default_output_dir_path() + 'asm6/'

    image_name_list: list = ["convollaria_512_10X_sameTracks_green.ics"]

    image_width: int = 512
    image_height: int = 512
    image_layers: int = 8

    gray_value_in_each_layer: list = [255, 225, 195, 165, 135, 105, 75, 45]

    for image_name in image_name_list:
        curr_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_diplib_image(image_name, input_dir);    ImageUtil.show_image_in_dip_view(curr_img)

        img_layers: list = []

        threshold_value = ImageUtil.derive_threshold_value(curr_img)
        threshold_img = ImageUtil.filter_image_by_threshold_value(curr_img, threshold_value)

        pixel_value_list = ImageUtil.obtain_pixel_value_list(curr_img)
        print(len(pixel_value_list))

        pixel_binary_stack = np.reshape(pixel_value_list, (image_layers, image_width, image_height))

        for layer_idx in range(0, image_layers):
            layer_img = np.zeros((image_width, image_height))
            for width_idx in range(image_width):
                for height_idx in range(image_height):
                    pixel_value = pixel_binary_stack[layer_idx][width_idx][height_idx]

                    if pixel_value == 1:
                        pixel_value = gray_value_in_each_layer[layer_idx]

                    layer_img[width_idx][height_idx] = pixel_value

            img_layers.append(layer_img)

        max_proj(img_layers, image_width, image_height)
        mean_proj(img_layers, image_width, image_height)

    CommonUtil.press_enter_to_exit()
