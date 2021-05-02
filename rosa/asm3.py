import diplib
import numpy as np

import diplib as dip
from PIL import Image as PilImage
import PIL
from diplib import PyDIPjavaio

import matplotlib.pyplot as plt

from util import UtilFunctions

if __name__ == '__main__':
    sleep_sec: int = 20

    '''
    # Part 3.2
    image_name_list: list = ["scale-img.ics"]

    for image_name in image_name_list:
        img = UtilFunctions.obtain_image(image_name)
        UtilFunctions.show_image_in_dip_view(img, sleep_sec)
        #print(img)

        #pixel_values = UtilFunctions.get_pixel_values(img)
        #UtilFunctions.get_histogram(pixel_values, image_name)

        #UtilFunctions.get_numerical_statistics(pixel_values, image_name)

        #UtilFunctions.save_image_to_default_project_folder(img, "test")

    '''
    # Part 3.1

    image_name_list = ["AxioCamIm02.tif"]

    for image_name in image_name_list:
        img = UtilFunctions.obtain_image(image_name)
        img = dip.Opening(img)
        UtilFunctions.save_image_to_default_project_folder(img, "asm3", "opening_" + image_name)

        even_background_img = UtilFunctions.black_hat_transf(img)
        UtilFunctions.save_image_to_default_project_folder(even_background_img, "asm3", "black_hat_" + image_name)

        kernel = dip.PyDIP_bin.Kernel(shape='rectangular', param=[30])
        no_noise_img = dip.MedianFilter(even_background_img, kernel)
        UtilFunctions.save_image_to_default_project_folder(no_noise_img, "asm3", "median_filter_" + image_name)

        segm_img = UtilFunctions.segment_image(no_noise_img)

        UtilFunctions.save_image_to_default_project_folder(segm_img, "asm3", "segm_" + image_name)

        UtilFunctions.calibrate(segm_img)


    '''
    # Part 3.3
    image_name_list = ["scale-img.tif"]

    for image_name in image_name_list:
        img = UtilFunctions.obtain_image(image_name)
        UtilFunctions.show_image_in_dip_view(img, sleep_sec)

        #background = UtilFunctions.gaussian_filter(img, 400)
        struct_elem = diplib.PyDIP_bin.SE(shape='elliptic', param=71)
        background = dip.Closing(img, struct_elem)
        UtilFunctions.show_image_in_dip_view(background, sleep_sec)

        new_img = background - img

        print(UtilFunctions.get_pixel_values(img))
        print(UtilFunctions.get_pixel_values(new_img))

        UtilFunctions.show_image_in_dip_view(new_img, sleep_sec)
    '''
