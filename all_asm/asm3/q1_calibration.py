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


    # filter 1 para 1
    for image_name in image_name_list:
        original_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_image(image_name, input_dir_str);   ImageUtil.show_image_in_dip_view(original_img, title="original img")

        filtered_img = ImageUtil.median_filter(original_img, "rectangular");   ImageUtil.show_image_in_dip_view(filtered_img, title="filtered_img")

        threshold_img = ImageUtil.obtain_threshold_image(filtered_img);     ImageUtil.show_image_in_dip_view(threshold_img, title="threshold_img")

        segment_size: int = 9
        erosion_img = ImageUtil.erosion(threshold_img, segment_size);     ImageUtil.show_image_in_dip_view(erosion_img, title="erosion_img")
        dilation_img = ImageUtil.dilation(threshold_img, segment_size);     ImageUtil.show_image_in_dip_view(dilation_img, title="dilation_img")

        # file_name = image_name + "_filter1_gauss_filter_para1_" + str(sigma_value) + ".tif"
        # CommonUtil.save_image_to_default_project_folder(img=original_img, dir_name=date_time_str, file_name=file_name)


        CommonUtil.press_enter_to_continue()


    CommonUtil.press_enter_to_continue()
