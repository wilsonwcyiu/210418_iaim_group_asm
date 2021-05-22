from diplib import PyDIPjavaio

from util.common_util import CommonUtil
from util.image_util import ImageUtil

# test_case

if __name__ == '__main__':
    print("starting...")
    sleep_sec: int = 0

    image_name_list: list = ["AxioCamIm01", "AxioCamIm02", "AxioCamIm03"]


    input_dir_str: str = CommonUtil.obtain_project_default_input_dir_path() + "asm3/"
    date_time_str: str = CommonUtil.generate_date_time_str()
    output_dir_str: str = CommonUtil.obtain_project_default_output_dir_path() + date_time_str


    # shape_list = ['rectangular', 'elliptic', 'diamond', 'parabolic']
    # se_lenght_list = [11, 21, 31, 41, 51, 61, 71]
    #
    # # filter 1 para 1
    # for shape in shape_list:
    #     for se_length in se_lenght_list:
    to_show_name_img_tuple_list = []

    for image_name in image_name_list:

        original_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_diplib_image(image_name, input_dir_str);   #ImageUtil.show_image_in_dip_view(original_img, title="original img")
        to_show_name_img_tuple_list.append(("original img " + image_name, original_img))


        # filtered_img = ImageUtil.median_filter(original_img, "rectangular");   #ImageUtil.show_image_in_dip_view(filtered_img, title="filtered_img")

        threshold_img = ImageUtil.obtain_threshold_image(original_img);     #ImageUtil.show_image_in_dip_view(threshold_img, title="threshold_img")
        to_show_name_img_tuple_list.append(("threshold_img " + image_name, threshold_img))



    x = 0
    x_pos = x
    y_pos = 0
    distance = 400
    print(len(to_show_name_img_tuple_list))
    for to_show_name_img_tuple in to_show_name_img_tuple_list:

        ImageUtil.show_image_in_dip_view(to_show_name_img_tuple[1], title=to_show_name_img_tuple[0], position_tuple=(x_pos, y_pos))

        x += distance

        x_pos = x % (distance * 5)
        y_pos = int(x/(distance * 5)) * distance
        print(x_pos, y_pos)


    print("output_dir_str", output_dir_str)
    CommonUtil.press_enter_to_continue()


    CommonUtil.press_enter_to_continue()
