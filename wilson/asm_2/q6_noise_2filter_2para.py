from diplib import PyDIPjavaio
from matplotlib import pyplot

from util.common_util import CommonUtil
from util.image_util import ImageUtil


# test
from util.plot_util import PlotUtil

if __name__ == '__main__':
    print("starting...")
    sleep_sec: int = 0

    image_name_list: list = ["rect1a", "rect2a", "rect3a", "rect4a",
                             "rect1b", "rect2b", "rect3b", "rect4b"]


    date_time_str: str = CommonUtil.generate_date_time_str()

    # filter 1 para 1
    for image_name in image_name_list:
        original_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_image(image_name)

        sigma_value: int = 2
        gauss_img = ImageUtil.gauss_filter(original_img, sigma_value)

        threshold_img = ImageUtil.obtain_threshold_image(gauss_img)

        ImageUtil.show_image_in_dip_view(threshold_img)

        file_name = image_name + "_filter1_gauss_filter_para1_" + str(sigma_value) + ".tif"

        CommonUtil.save_image_to_default_project_folder(img=original_img, dir_name=date_time_str, file_name=file_name)



    # filter 1 para 2
    for image_name in image_name_list:
        original_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_image(image_name)

        sigma_value: int = 3
        gauss_img = ImageUtil.gauss_filter(original_img, sigma_value)

        threshold_img = ImageUtil.obtain_threshold_image(gauss_img)

        ImageUtil.show_image_in_dip_view(threshold_img)

        file_name = image_name + "_filter1_gauss_filter_para2_" + str(sigma_value) + ".tif"

        CommonUtil.save_image_to_default_project_folder(img=threshold_img, dir_name=date_time_str, file_name=file_name)



    # filter 2 para 1
    for image_name in image_name_list:
        original_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_image(image_name)

        median_para: str = 'rectangular'
        median_img = ImageUtil.median_filter(original_img, median_para)

        threshold_img = ImageUtil.obtain_threshold_image(median_img)

        ImageUtil.show_image_in_dip_view(threshold_img)

        file_name = image_name + "_filter1_median_filter_para1_" + str(median_para) + ".tif"

        CommonUtil.save_image_to_default_project_folder(img=threshold_img, dir_name=date_time_str, file_name=file_name)



    # filter 2 para 2
    for image_name in image_name_list:
        original_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_image(image_name)

        median_para: str = 'elliptic'
        median_img = ImageUtil.median_filter(original_img, median_para)

        threshold_img = ImageUtil.obtain_threshold_image(median_img)

        ImageUtil.show_image_in_dip_view(threshold_img)

        file_name = image_name + "_filter1_median_filter_para2_" + str(median_para) + ".tif"

        CommonUtil.save_image_to_default_project_folder(img=threshold_img, dir_name=date_time_str, file_name=file_name)



    CommonUtil.press_enter_to_continue()
