import pprint

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
    # image_name: str = "AxioCamIm02_high_contrast_threshold_img_elliptic_91.tif"
    # image_name: str = "AxioCamIm03_high_contrast_threshold_img_elliptic_181.tif"


    threshold_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_image(image_name, input_dir_str)

    column_pixel_tuple_list: list = ImageUtil.obtain_column_pixel_value_list(threshold_img)    # print("col cnt", len(pixel_column_tuple_list));  print("row cnt", len(pixel_column_tuple_list[0]))

    # extract right most 20% region of the image by column
    start_col = int(len(column_pixel_tuple_list) * 0.8)
    column_pixel_tuple_list = column_pixel_tuple_list[start_col:]


    # column_mixed_pixel_tuple_list: list = []
    # for column_pixel_tuple in column_pixel_tuple_list:
    #     if 1 in column_pixel_tuple:
    #         column_mixed_pixel_tuple_list.append(column_pixel_tuple)


    pixel_change_count_tuple_dict: {} = {}    #key: change count. value: pixel_value_tuple_list
    for col_idx in range(0, len(column_pixel_tuple_list)):
        column_pixel_tuple = column_pixel_tuple_list[col_idx]
        last_col_value: int = column_pixel_tuple[0]
        change_cnt: int = 0

        for tuple_idx in range(1, len(column_pixel_tuple)):
            column_pixel: int = column_pixel_tuple[tuple_idx]
            if column_pixel != last_col_value:
                change_cnt += 1
                last_col_value = column_pixel

        if change_cnt not in pixel_change_count_tuple_dict:
            pixel_change_count_tuple_dict[change_cnt] = []

        pixel_change_count_tuple_dict[change_cnt].append(column_pixel_tuple)


    for key, item in pixel_change_count_tuple_dict.items():
        print("change_count:", key, ". total_col_count", len(item)) #, "->> columns idx: ", str(item))


    # for column_pixel_tuple in column_pixel_tuple_list:
    #     for column_pixel in column_pixel_tuple:
    #         print(column_pixel, end="")
    #     print()


    most_same_cnt_column_tuple_list: list = []    # list of column_idx that has the same change coun
    most_same_column_cnt: int = 0
    for change_cnt, column_tuple_list in pixel_change_count_tuple_dict.items():
        if len(column_tuple_list) > most_same_column_cnt:
            most_same_column_cnt = len(column_tuple_list)
            most_same_cnt_column_tuple_list = column_tuple_list

    print("most_same_column_cnt", most_same_column_cnt)
    # print("most_same_cnt_column_list", most_same_cnt_column_tuple_list)



    scale_pixel_column_tuple: tuple = most_same_cnt_column_tuple_list[0]

    scale_pixel_width_list: list = []
    last_start_pixel: int = None
    last_pixel_value: int = None
    for idx in range(0, len(scale_pixel_column_tuple)):
        current_pixel: int = scale_pixel_column_tuple[idx]

        is_pixel_changed_from_black_to_white: bool = (last_pixel_value == 0 and current_pixel == 1)

        if is_pixel_changed_from_black_to_white:
            if last_start_pixel is not None:
                pixel_width: int = idx - last_start_pixel
                scale_pixel_width_list.append(pixel_width)
            last_start_pixel = idx

        last_pixel_value = current_pixel

    print("scale_pixel_width_list", scale_pixel_width_list)

    pixel_length_value: float = 0.01 / CommonUtil.calc_mean(scale_pixel_width_list)
    print("pixel_length_value", pixel_length_value)


    CommonUtil.press_enter_to_continue()
