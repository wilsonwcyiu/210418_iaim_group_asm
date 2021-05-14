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
        print("Analysis of ", image_name)
        curr_img = ImageUtil.obtain_image(image_name, input_dir)
        # Get general information about the image
        print(curr_img)

        # Look at differences visually
        ImageUtil.show_image_in_dip_view(curr_img, sleep_sec, image_name)
        # Get list of the pixel values of current image
        pixel_values = ImageUtil.obtain_pixel_value_list(curr_img)

        # Get numerical information about the current image
        min_value = min(pixel_values)
        max_value = max(pixel_values)
        mean_value = np.mean(pixel_values)

        print("Minimum intensity value of ", image_name, ": ", min_value)
        print("Maximum intensity value of ", image_name, ": ", max_value)

        print("Average intensity value of ", image_name, ": ", mean_value)

        # Generate histogram of current image and show the plot
        histogram = PlotUtil.create_histogram_plot_depricated(1, 'Histogram of ' + image_name, 'Intensity values', 'Frequency', pixel_values, list(range(int(min_value), int(max_value))))
        histogram.show()