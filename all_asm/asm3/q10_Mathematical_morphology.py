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

    se_shape = 'elliptic'
    se_size = 21

    print("SE:", se_shape, "size:", se_size)

    original_image = ImageUtil.obtain_image(image_name, input_dir_str)

    black_hat_image = ImageUtil.black_hat(original_image, se_size, se_shape)

    file_name = image_name + "_black_hat_" + se_shape + "_" + str(se_size)
    ImageUtil.show_image_in_dip_view(black_hat_image, 20, file_name)

    # CommonUtil.save_image_to_folder(black_hat_image, output_dir_str, file_name + ".tif")

    # Segmentation
    segmented_image = ImageUtil.segment_image_white(black_hat_image)

    file_name = file_name + '_segmented'
    print(file_name)
    ImageUtil.show_image_in_dip_view(segmented_image, 20, file_name)
    # CommonUtil.save_image_to_folder(segmented_image, output_dir_str, file_name + ".tif")

