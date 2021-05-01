import os

import diplib as dip
import numpy as np
import matplotlib.pyplot as plt

from util.common_util import CommonUtil
from util.image_util import ImageUtil






if __name__ == '__main__':

    image_name = 'scale-img'

    input_dir_str: str = CommonUtil.obtain_project_default_input_dir_path() + "asm3/"
    date_time_str: str = CommonUtil.generate_date_time_str()
    output_dir_str: str = CommonUtil.obtain_project_default_output_dir_path() + date_time_str + "_q8_Math_morp/"
    CommonUtil.create_missing_dir(output_dir_str)

    se_shape = ['elliptic', 'diamond', 'rectangular']
    se_size = [5, 11, 21, 31, 51]

    for se in se_shape:
        for size in se_size:
            print("SE:", se, "size:", size)

            original_image = ImageUtil.obtain_image(image_name, input_dir_str)

            # Black Hat transformation
            black_hat_image = ImageUtil.black_hat(original_image, size, se)
            file_name = image_name + "_black_hat_" + se + "_" + str(size) + ".tif"
            ImageUtil.show_image_in_dip_view(black_hat_image, 20, file_name)
            CommonUtil.save_image_to_folder(black_hat_image, output_dir_str, file_name)
