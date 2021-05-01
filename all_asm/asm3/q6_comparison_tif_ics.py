import numpy as np
import diplib as dip
from diplib import PyDIPjavaio
import matplotlib.pyplot as plt

from util.common_util import CommonUtil
from util.image_util import ImageUtil
from util.plot_util import PlotUtil

if __name__ == '__main__':
    sleep_sec: int = 10

    input_dir: str = CommonUtil.obtain_project_default_input_dir_path() + "asm3/"

    image_name_list: list = ["scale-img.tif", "scale-img.ics"]

    for image_name in image_name_list:
        img = UtilFunctions.obtain_image(image_name, input_dir)
        print(img)

        #UtilFunctions.show_image_in_dip_view(img, sleep_sec)

        #pixel_values = UtilFunctions.get_pixel_values(img)
        #UtilFunctions.get_histogram(pixel_values, image_name)

        #UtilFunctions.get_numerical_statistics(pixel_values, image_name)

        #UtilFunctions.save_image_to_default_project_folder(img, "test")