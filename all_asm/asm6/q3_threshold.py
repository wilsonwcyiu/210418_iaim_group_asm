import dip as dip
import diplib
from diplib import PyDIPjavaio
from PIL import Image

from util.common_util import CommonUtil
from util.image_util import ImageUtil
from util.plot_util import PlotUtil
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np


if __name__ == '__main__':

    # Configure files and directories
    input_dir: str = CommonUtil.obtain_project_default_input_dir_path() + 'asm6/'
    proj_output_dir_path: str = CommonUtil.obtain_project_default_output_dir_path() + CommonUtil.generate_date_time_str() + "/"

    image_width: int = 140
    image_height: int = 160
    image_layers: int = 16

    image_name_list: list = ["CHROMO3D.ics"]

    CommonUtil.make_dir(proj_output_dir_path)




    for image_name in image_name_list:
        curr_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_diplib_image(image_name, input_dir);        ImageUtil.show_image_in_dip_view(curr_img)

        threshold_value = ImageUtil.derive_threshold_value(curr_img);        print(threshold_value)
        # threshold_value = 60;        print(threshold_value)
        # threshold_value = 75;        print(threshold_value)

        threshold_img = ImageUtil.filter_image_by_threshold_value(curr_img, threshold_value);        ImageUtil.show_image_in_dip_view(threshold_img)

        pixel_flattened_list = ImageUtil.obtain_pixel_value_list(threshold_img)
        pixel_binary_3d = np.reshape(pixel_flattened_list, (image_layers, image_width, image_height));        #ImageUtil.show_image_in_dip_view(pixel_binary_3d, title="pixel_3d")


        for layer_idx in range(0, 16):
            pixel_grayscale_2d = np.zeros((image_width, image_height))
            for width_idx in range(image_width):
                for height_idx in range(image_height):
                    pixel_value = pixel_binary_3d[layer_idx][width_idx][height_idx]

                    pixel_grayscale_2d[width_idx][height_idx] = pixel_value

            file_name: str = "layer_" + str(layer_idx) + "_threshold_" + str(threshold_value) + ".png"
            # file_name: str = "layer_" + str(layer_idx) + "_original_img.png"
            CommonUtil.save_ndarray_as_image(pixel_grayscale_2d, proj_output_dir_path, file_name)




        # threshold2_img = ImageUtil.segment_image_white(curr_img);                                ImageUtil.show_image_in_dip_view(threshold2_img)









        # p_list = ImageUtil.obtain_pixel_value_list(curr_img)
        # plot = PlotUtil.create_histogram_plot(p_list)
        # plot.show()


        # print(curr_img)
        # diplib.ImageRead
        # diplib.Image
        # print(type(curr_img))

        # print(curr_img[1])
        # for pixel_location in range(len(curr_img)):
        #     print(pixel_location)
            # pixel_value = curr_img[pixel_location][0]
            # pixel_value_list.append(pixel_value)


        # pixel_list = ImageUtil.obtain_pixel_value_list(curr_img)
        # print(pixel_list.shape)

        # diplib.ShowViewer(curr_img)
        # squeeze(curr_img(:,:,2))

        # DataType : # https://diplib.org/diplib-docs/pixeltypes.html
        # curr_img = diplib.Convert(curr_img, "UINT8")

        # print(curr_img(1,1,1))

        # pixel_value_list = ImageUtil.obtain_pixel_value_list(curr_img)
        # plot = PlotUtil.create_histogram_plot(pixel_value_list)
        # plot.show()

        # data_type = dip::DT_UINT8
        # diplib.Convert(curr_img, dt=)

        # ImageUtil.show_image_in_dip_view(threshold_img)


    CommonUtil.press_enter_to_exit()