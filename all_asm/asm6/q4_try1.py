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




    image_name_list: list = ["CHROMO3D.ICS"]

    for image_name in image_name_list:
        curr_img: diplib.PyDIP_bin.Image = ImageUtil.obtain_diplib_image(image_name, input_dir);        ImageUtil.show_image_in_dip_view(curr_img)


        ImageUtil.show_image_in_dip_view(curr_img.Squeeze())


        CommonUtil.press_enter_to_exit()


        data_list = numpy.array([[1,1,1,1],[0,0,0,0]])

        ImageUtil.show_image_in_dip_view(data_list)

        CommonUtil.press_enter_to_exit()

        # print(type(a), a)


        curr_img.setProjectionMode("max")

        threshold_value = ImageUtil.derive_threshold_value(curr_img)
        print(threshold_value)
        threshold_img = ImageUtil.filter_image_by_threshold_value(curr_img, 75);        ImageUtil.show_image_in_dip_view(threshold_img)


        t2_img = ImageUtil.segment_image_white(curr_img);                                ImageUtil.show_image_in_dip_view(t2_img)


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