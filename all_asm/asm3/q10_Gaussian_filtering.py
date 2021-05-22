import diplib as dip
import numpy as np
import matplotlib.pyplot as plt

from util.common_util import CommonUtil
from util.image_util import ImageUtil






if __name__ == '__main__':

    # We can observe in the image that on the longer axis
    # there are in total 22 units and we will use that
    # as a constant for measurement of pixels per unit
    number_of_units_on_longer_axis: int = 22

    image_name = 'scale-img'

    input_dir_str: str = CommonUtil.obtain_project_default_input_dir_path() + "asm3/"
    output_dir_str: str = CommonUtil.obtain_project_default_output_dir_path() + "q8/"
    CommonUtil.create_missing_dir(output_dir_str)
    date_time_str: str = CommonUtil.generate_date_time_str()


    # sigma = 10 is the chosen value, based on the segmented image
    sigma = 10
    print("sigma:", sigma)

    original_image = ImageUtil.obtain_diplib_image(image_name, input_dir_str)


    # Gaussian filtering
    gauss_image = ImageUtil.gauss_filter(original_image, sigma)
    file_name = image_name + "_gauss_" + str(sigma)
    print(file_name)
    ImageUtil.show_image_in_dip_view(gauss_image, 10, file_name)
    # CommonUtil.save_image_to_folder(gauss_image, output_dir_str, file_name + ".tif")


    # Difference
    # subtracting the original image from output of gaussian filter on original image
    # to get similar filter as black top-hat filter
    difference = gauss_image - original_image
    file_name = file_name + "_difference"
    ImageUtil.show_image_in_dip_view(difference, 10, file_name)
    # CommonUtil.save_image_to_folder(difference, output_dir_str, file_name)


    # Segmentation of difference
    segmented_image = ImageUtil.segment_image_white(difference)
    file_name = file_name + '_segmented'
    print(file_name)
    ImageUtil.show_image_in_dip_view(segmented_image, 10, file_name)
    # CommonUtil.save_image_to_folder(segmented_image, output_dir_str, file_name + ".tif")


    # MEASUREMENT
    # Setting the minSize to 50, assuming that only the squares and the scale will remain in the image
    labeled_image = dip.Label(segmented_image, minSize=50)
    feret_measurement = dip.MeasurementTool.Measure(labeled_image, difference, ['Size', 'Feret'] )
    print(feret_measurement)

    # The biggest object has label 3
    size_scale_object = feret_measurement[3]['Size']
    print("Size of scale object:", size_scale_object)

    feret_scale_object = feret_measurement[3]['Feret']
    print("Feret:", feret_scale_object)
    max_feret = max(feret_scale_object)
    print("Max feret diameter:", max_feret, "[px]")
    print("Number of units on longer scale:", number_of_units_on_longer_axis)

    # Now we know the number of pixels and number of units
    # PIXEL SIZE
    # Units per pixel
    units_per_pixel = number_of_units_on_longer_axis / max_feret
    print("Units  per pixel:", units_per_pixel, "[units/px]")












