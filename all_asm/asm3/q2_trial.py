import diplib
from diplib import PyDIPjavaio

from util.common_util import CommonUtil
from util.image_util import ImageUtil

# test_case
from util.plot_util import PlotUtil

if __name__ == '__main__':
    print("starting...")
    sleep_sec: int = 0

    input_dir_str: str = CommonUtil.obtain_project_default_input_dir_path() + "asm3/"
    date_time_str: str = CommonUtil.generate_date_time_str()
    output_dir_str: str = CommonUtil.obtain_project_default_output_dir_path() + date_time_str + "/"
    CommonUtil.create_missing_dir(output_dir_str)


    image_name: str = "AxioCamIm01_high_contrast_threshold_img_elliptic_71.tif"

    pixel_column_tuple_list: list = []       #pixel_column_tuple_list[(pixel_value_tuple)]      e.g. [ (0,0,1,1,0), (0,1,1,1,0)  ]

    max_pixel_change_count: int = None

    scale_pixel_column_tuple_list: list = []
    for pixel_column_tuple in pixel_column_tuple_list:
        pixel_change_count: int = None
        if pixel_change_count == max_pixel_change_count:
            scale_pixel_column_tuple_list.append(pixel_column_tuple)



    scale_pixel_column_tuple: tuple = scale_pixel_column_tuple_list[0]
    scale_start_pixel_idx: int = None
    scale_end_pixel_idx: int = None


    scale_pixel_width_list: list = []
    pixel_count: int = 0
    last_pixel_value: int = 1
    for i in range(scale_start_pixel_idx, scale_end_pixel_idx):
        current_pixel: int = scale_pixel_column_tuple[current_pixel]
        is_pixel_changed_from_black_to_white: bool = (last_pixel_value == 0 and current_pixel == 1)

        if is_pixel_changed_from_black_to_white:
            scale_pixel_width_list.append(pixel_count)
            pixel_count = 0
        else:
            pixel_count += 1

        last_pixel_value = current_pixel


    pixel_length_value: float = 0.01 / CommonUtil.calc_mean(scale_pixel_width_list)
    print("pixel_length_value", pixel_length_value)



    CommonUtil.press_enter_to_continue()
