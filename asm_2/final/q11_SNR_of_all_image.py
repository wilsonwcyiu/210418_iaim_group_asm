import diplib
from diplib import PyDIPjavaio
from matplotlib import pyplot

from util.common_util import CommonUtil
from util.image_util import ImageUtil
import pprint

# test
from util.plot_util import PlotUtil

if __name__ == '__main__':
    print("starting...")
    sleep_sec: int = 0

    image_name_list: list = [
                            "rect1", "rect2", "rect3", "rect4",
                            "rect1a", "rect2a", "rect3a", "rect4a",
                            "rect1b", "rect2b", "rect3b", "rect4b"
                            ]


    # date_time_str: str = CommonUtil.generate_date_time_str()
    # output_dir: str = CommonUtil.obtain_project_default_output_file_path() + date_time_str + "/"

    result_dict_list: list = []
    for image_name in image_name_list:
        original_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_image(image_name)

        snr: float = ImageUtil.calculate_signal_to_noise_ratio_SNR(original_img)
        result_dict: dict = {
                            "image_name": image_name,
                             "snr": snr
                            }

        result_dict_list.append(result_dict)

    CommonUtil.pretty_print(result_dict_list)


    # print("output folder " + output_dir)
    CommonUtil.press_enter_to_continue()
