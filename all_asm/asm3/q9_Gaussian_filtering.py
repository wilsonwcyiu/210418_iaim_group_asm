import diplib as dip
import numpy as np
import matplotlib.pyplot as plt

from util.common_util import CommonUtil
from util.image_util import ImageUtil






if __name__ == '__main__':

    image_name = 'scale-img.tif'

    input_dir_str: str = CommonUtil.obtain_project_default_input_dir_path() + "asm3/"
    date_time_str: str = CommonUtil.generate_date_time_str()
    output_dir_str: str = CommonUtil.obtain_project_default_output_dir_path() + date_time_str + "_q9_gauss/"
    CommonUtil.create_missing_dir(output_dir_str)

    # different sigma values
    sigma = [1, 2, 3, 4, 5, 10, 15, 20, 30, 50]

    for value in sigma:
        print("sigma:", sigma)

        original_image = ImageUtil.obtain_diplib_image(image_name, input_dir_str)

        # Gaussian filtering
        gauss_image = ImageUtil.gauss_filter(original_image, value)
        file_name = image_name + "_gauss_" + str(value)
        print(file_name)
        # ImageUtil.show_image_in_dip_view(gauss_image, 10, file_name + ".tif")
        # CommonUtil.save_image_to_folder(gauss_image, output_dir_str, file_name)


        # Difference
        # subtracting the original image from output of gaussian filter on original image
        # to get similar filter as black top-hat filter
        difference = gauss_image - original_image
        file_name = image_name + "_gauss_" + str(value) + "_difference"
        # ImageUtil.show_image_in_dip_view(difference, 20, file_name + ".tif")
        # CommonUtil.save_image_to_folder(difference, output_dir_str, file_name)


        # Segmentation of difference
        segmented_image = ImageUtil.segment_image_white(difference)
        file_name = file_name + '_segmented'
        print(file_name)
        ImageUtil.show_image_in_dip_view(segmented_image, 10, file_name)
        # CommonUtil.save_image_to_folder(segmented_image, output_dir_str, file_name + ".tif")















