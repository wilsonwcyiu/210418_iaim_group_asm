import diplib
import numpy as np

import diplib as dip
from PIL import Image as PilImage
import PIL
from diplib import PyDIPjavaio

import matplotlib.pyplot as plt

from util import UtilFunctions

if __name__ == '__main__':
    sleep_sec: int = 10

    # Part 3.2
    '''
    image_name_list: list = ["scale-img.tif", "scale-img.ics"]

    for image_name in image_name_list:
        img = UtilFunctions.obtain_image(image_name)
        #UtilFunctions.show_image_in_dip_view(img, sleep_sec)
        print(img)

        print(img[0])

        pixel_values = UtilFunctions.get_pixel_values(img)
        UtilFunctions.get_histogram(pixel_values, image_name)

        UtilFunctions.get_numerical_statistics(pixel_values, image_name)
    '''

    image_name_list = ["AxioCamIm02.tif"]

    for image_name in image_name_list:
        img = UtilFunctions.obtain_image(image_name)
        #UtilFunctions.show_image_in_dip_view(img, sleep_sec)

        img = UtilFunctions.black_hat_transf(img)

        UtilFunctions.show_image_in_dip_view(img, sleep_sec)

        kernel = dip.PyDIP_bin.Kernel(shape='rectangular', param=[30])
        img = dip.MedianFilter(img, kernel)

        img = UtilFunctions.segment_image(img)
        UtilFunctions.show_image_in_dip_view(img, sleep_sec)
