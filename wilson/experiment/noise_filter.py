import diplib
import numpy as np

from diplib import PyDIPjavaio

from util.common_util import CommonUtil
from util.image_util import ImageUtil
from util.plot_util import PlotUtil

if __name__ == '__main__':
    print("starting...")
    sleep_sec: int = 0



    image_name_list: list = []
    # image_name_list.append("rect1" )
    # image_name_list.append("rect1a")
    # image_name_list.append("rect1b")
    #
    # image_name_list.append("rect2" )
    # image_name_list.append("rect2a")
    # image_name_list.append("rect2b")
    #
    # image_name_list.append("rect3" )
    # image_name_list.append("rect3a")
    # image_name_list.append("rect3b")
    #
    # image_name_list.append("rect4" )
    # image_name_list.append("rect4a")
    image_name_list.append("rect4b")


    date_time_str: str = CommonUtil.generate_date_time_str()

    # filter 1 para 1
    for image_name in image_name_list:
        original_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_diplib_image(image_name)

        sigma_value: int = 3.2
        gauss_img = ImageUtil.gauss_filter(original_img, sigma_value)

        threshold_img = ImageUtil.obtain_threshold_image(gauss_img)

        ImageUtil.show_image_in_dip_view(original_img, title="original_img")
        ImageUtil.show_image_in_dip_view(gauss_img, title="gauss_img")
        ImageUtil.show_image_in_dip_view(threshold_img, title="threshold_img")

        number_of_objects: int = ImageUtil.detect_number_of_objects(threshold_img, original_img)
        print("number_of_objects", number_of_objects)

        pixel_value_list: list = ImageUtil.obtain_pixel_value_list(gauss_img)

        plot_id: int = 1
        plot_title: str = "Image Histogram"
        x_label: str = "Intensity value"
        y_label: str = "Count"
        plt = PlotUtil.create_histogram_plot_depricated(plot_id, plot_title, x_label, y_label, pixel_value_list)
        plt.show()





    print("end")
    CommonUtil.press_enter_to_continue()