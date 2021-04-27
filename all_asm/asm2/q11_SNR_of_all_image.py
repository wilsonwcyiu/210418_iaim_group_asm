import math

import diplib
from diplib import PyDIPjavaio
from matplotlib import pyplot

from util.common_util import CommonUtil
from util.image_util import ImageUtil
import pprint

# test_case
from util.plot_util import PlotUtil

if __name__ == '__main__':
    print("starting...")
    sleep_sec: int = 0



    image_name_dict: dict = {
                             "img1": ["rect1", "rect1a", "rect1b"],
                             "img2": ["rect2", "rect2a", "rect2b"],
                             "img3": ["rect3", "rect3a", "rect3b"],
                             "img4": ["rect4", "rect4a", "rect4b"],
                             }




    date_time_str: str = CommonUtil.generate_date_time_str()
    output_dir: str = CommonUtil.obtain_project_default_output_dir_path() + date_time_str + "/"

    result_dict_list: list = []

    for img_group_name, img_list in image_name_dict.items():
        xy_tuple_list: list = []
        for image_name in img_list:
            original_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_image(image_name)

            snr: float = ImageUtil.calculate_signal_to_noise_ratio_SNR(original_img)
            log_snr: float = math.log(snr)

            xy_tuple_list.append((image_name, log_snr))

            result_dict: dict = {
                                "image_name": image_name,
                                 "Decibel - log(SNR) value": log_snr
                                }
            result_dict_list.append(result_dict)

        plot_id: int = 1
        plot_title: str = "SNR against the log(measurement)"
        x_label: str = "Image name"
        y_label: str = "Decibel - log(SNR) value"
        plot = PlotUtil.create_plot(plot_id, plot_title, x_label, y_label, xy_tuple_list)

        file_name: str = img_group_name + "_snr_plot"
        PlotUtil.save_plot_to_folder(plot, output_dir, file_name)





    CommonUtil.pretty_print(result_dict_list)



    print("output folder " + output_dir)
    CommonUtil.press_enter_to_continue()
