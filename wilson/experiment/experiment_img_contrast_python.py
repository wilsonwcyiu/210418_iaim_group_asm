import os

import diplib
import numpy as np

from diplib import PyDIPjavaio
from diplib.PyDIP_bin import SE
from matplotlib import pyplot

from util.common_util import CommonUtil
from util.image_util import ImageUtil


from PIL import Image as PIL_IMAGE, ImageEnhance

# test_case
from util.plot_util import PlotUtil

if __name__ == '__main__':
    print("starting...")
    sleep_sec: int = 0

    image_name_list: list = ["AxioCamIm01", "AxioCamIm02", "AxioCamIm03"]

    input_dir_str: str = "D:/Wilson/PycharmProjects/210418_iaim_group_asm/image_files/asm3/" #CommonUtil.obtain_project_default_input_dir_path()# + "asm3/"

    date_time_str: str = CommonUtil.generate_date_time_str()
    output_dir_str: str = "D:/Wilson/PycharmProjects/210418_iaim_group_asm/file_output/" + date_time_str + "/" #CommonUtil.obtain_project_default_output_dir_path() + date_time_str + "_" + os.path.basename(__file__) + "/"
    CommonUtil.make_dir(output_dir_str)


    for image_name in image_name_list:
        #read the image
        pil_img = PIL_IMAGE.open(input_dir_str + image_name + ".tif")

        #image brightness enhancer
        enhancer = ImageEnhance.Contrast(pil_img)

        # factor = 0.5 #decrease constrast
        # factor = 1 #gives original image
        factor = 2.5 #increase contrast
        im_output = enhancer.enhance(factor)

        file_name = image_name + "_high_contrast.tif"
        file_path = output_dir_str + file_name
        im_output.save(file_path)

        img = ImageUtil.obtain_diplib_image(file_path, "")
        ImageUtil.show_image_in_dip_view(img)



        original_img = ImageUtil.obtain_diplib_image(file_name, input_dir_str)
        obtain_pixel_value_list = ImageUtil.obtain_pixel_value_list(original_img)
        plot_id: int = 1
        plot_title: str = file_name
        x_label: str = "x"
        y_label: str = "y"
        plot = PlotUtil.create_histogram_plot_depricated(plot_id, plot_title, x_label, y_label, obtain_pixel_value_list)
        plot.pause(10)




    # for image_name in image_name_list:
    #     original_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_image(image_name, dir_path=input_dir_str);        ImageUtil.show_image_in_dip_view(original_img, title="original_img")
    #     median_filter = ImageUtil.median_filter(original_img, "rectangular");                                    ImageUtil.show_image_in_dip_view(median_filter, title="median_filter")
    #     threshold_img = ImageUtil.obtain_threshold_image(median_filter);                                         ImageUtil.show_image_in_dip_view(threshold_img, title="threshold_img")
    #
    #     se_one_side_length: int = 9
    #     se_shape: str = "rectangular"
    #     # se: SE = diplib.PyDIP_bin.SE(shape=se_shape, param=se_one_side_length)
    #
    #
    #     black_hat_img_dip = black_hat_img = ImageUtil.black_hat(threshold_img, se_one_side_length, se_shape);           CommonUtil.save_image_to_folder(black_hat_img_dip, output_dir_str, "black_hat_img_dip.tif")
    #
    #     # black_hat_img_code = ImageUtil.opening(threshold_img, se_one_side_length, se_shape) < threshold_img;           CommonUtil.save_image_to_folder(black_hat_img_code, output_dir_str, "black_hat_img_code.tif")






    # black_hat_img: diplib.PyDIP_bin.Image = ImageUtil.opening(threshold_img, se_one_side_length, se_shape) < threshold_img




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