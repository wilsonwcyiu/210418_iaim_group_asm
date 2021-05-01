import diplib as dip
import numpy as np
import matplotlib.pyplot as plt

from util.common_util import CommonUtil
from util.image_util import ImageUtil






if __name__ == '__main__':

    image_name = 'scale-img'

    input_dir_str: str = CommonUtil.obtain_project_default_input_dir_path() + "asm3/"
    output_dir_str: str = CommonUtil.obtain_project_default_output_dir_path() + "q8/"
    CommonUtil.create_missing_dir(output_dir_str)


    # sigma = 1 is the chosen value, because it is least blurred
    sigma = 1
    print("sigma:", sigma)

    original_image = ImageUtil.obtain_image(image_name, input_dir_str)

    # Gaussian filtering
    gauss_image = ImageUtil.gauss_filter(original_image, sigma)

    file_name = image_name + "_gauss_" + str(sigma)
    print(file_name)
    ImageUtil.show_image_in_dip_view(gauss_image, 20, file_name)
    # CommonUtil.save_image_to_folder(gauss_image, output_dir_str, file_name + ".tif")


    # Segmentation
    segmented_image = ImageUtil.segment_image_black(gauss_image)

    file_name = file_name + '_segmented'
    print(file_name)
    ImageUtil.show_image_in_dip_view(segmented_image, 20, file_name)
    # CommonUtil.save_image_to_folder(segmented_image, output_dir_str, file_name + ".tif")

    # Segmentation of original
    segmented_original = ImageUtil.segment_image_black(original_image)

    file_name = image_name + '_segmented'
    print(file_name)
    ImageUtil.show_image_in_dip_view(segmented_original, 20, file_name)













