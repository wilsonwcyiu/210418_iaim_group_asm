import diplib
from diplib import PyDIPjavaio
from diplib.PyDIP_bin import SE

from util.common_util import CommonUtil
from util.image_util import ImageUtil

# test_case

if __name__ == '__main__':
    print("starting...")
    input_dir_str: str = CommonUtil.obtain_project_default_input_dir_path() + "asm3/"


    image_name_list: str = "AxioCamIm01";    se_one_side_length: int = 71;    se_shape: str = "elliptic";    median_kernel_length: int = 5
    # image_name_list: str = "AxioCamIm02";    se_one_side_length: int = 91;    se_shape: str = "elliptic";    median_kernel_length: int = 5
    # image_name_list: str = "AxioCamIm03";    se_one_side_length: int = 181;   se_shape: str = "elliptic";    median_kernel_length: int = 10

    input_dir_str: str = CommonUtil.obtain_project_default_input_dir_path() + "asm3/"
    original_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_image(image_name, input_dir_str);   #ImageUtil.show_image_in_dip_view(original_img, title="original img")

    high_contrast_image = diplib.ContrastStretch(original_img, method="linear")

    structuring_element: SE = diplib.PyDIP_bin.SE(shape=se_shape, param=se_one_side_length)
    black_hat_img = diplib.Tophat(high_contrast_image, se=structuring_element, polarity="black");        #ImageUtil.show_image_in_dip_view(original_img, title="original img")

    median_filtered_img = diplib.MedianFilter(black_hat_img, median_kernel_length)

    _, threshold_value = diplib.Threshold(median_filtered_img, method = 'otsu')
    threshold_img: diplib.PyDIP_bin.Image = median_filtered_img < threshold_value

    column_pixel_tuple_list: list = ImageUtil.obtain_column_pixel_value_list(threshold_img)    # print("col cnt", len(pixel_column_tuple_list));  print("row cnt", len(pixel_column_tuple_list[0]))


    # extract right most 20% region of the image by column
    start_col = int(len(column_pixel_tuple_list) * 0.8)
    column_pixel_tuple_list = column_pixel_tuple_list[start_col:]

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

    most_same_cnt_column_tuple_list: list = []    # list of column_idx that has the same pixel value change count
    most_same_column_cnt: int = 0
    for change_cnt, column_tuple_list in pixel_change_count_tuple_dict.items():
        if len(column_tuple_list) > most_same_column_cnt:
            most_same_column_cnt = len(column_tuple_list)
            most_same_cnt_column_tuple_list = column_tuple_list

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


    pixel_length_value: float = 0.01 / CommonUtil.calc_mean(scale_pixel_width_list)
    print("pixel_length_value", pixel_length_value)


    CommonUtil.press_enter_to_continue()
