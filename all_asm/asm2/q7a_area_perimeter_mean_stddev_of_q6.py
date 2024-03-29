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

    image_name_list: list = ["rect1a", "rect2a", "rect3a", "rect4a",
                             "rect1b", "rect2b", "rect3b", "rect4b"]


    date_time_str: str = CommonUtil.generate_date_time_str()
    output_dir: str = CommonUtil.obtain_project_default_output_dir_path() + date_time_str + "/"

    result_dict_list: list = []

    # filter 1 para 1
    for image_name in image_name_list:
        original_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_diplib_image(image_name)

        sigma_value: int = 2
        gauss_img = ImageUtil.gauss_filter(original_img, sigma_value)
        threshold_img = ImageUtil.obtain_threshold_image(gauss_img)

        file_name = image_name + "_filter1_gauss_filter_para1_" + str(sigma_value) + ".tif"
        CommonUtil.save_image_to_folder(img=threshold_img, dir_path_str=output_dir, file_name=file_name)


        surface_area_list: list = ImageUtil.measure_surface_area_of_all_objects(threshold_img, original_img)
        surface_area_mean: float = CommonUtil.calc_mean(surface_area_list)
        surface_area_std_dev: float = CommonUtil.calc_standard_deviation(surface_area_list, surface_area_mean)

        perimeter_list: list = ImageUtil.measure_perimeter_of_all_objects(threshold_img, original_img)
        perimeter_mean: float = CommonUtil.calc_mean(perimeter_list)
        perimeter_std_dev: float = CommonUtil.calc_standard_deviation(perimeter_list, perimeter_mean)


        result_dict: dict = {}
        result_dict["image_name"] = image_name
        result_dict["filter_name"] = "filter"
        result_dict["parameter"] = "signma: " + str(sigma_value)

        result_dict["surface_area_list"] = str(surface_area_list)
        result_dict["surface_area_mean"] = surface_area_mean
        result_dict["surface_area_std_dev"] = surface_area_std_dev

        result_dict["perimeter_list"] = str(perimeter_list)
        result_dict["perimeter_mean"] = perimeter_mean
        result_dict["perimeter_std_dev"] = perimeter_std_dev

        result_dict_list.append(result_dict)



    # filter 1 para 2
    for image_name in image_name_list:
        original_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_diplib_image(image_name)

        sigma_value: int = 3
        gauss_img = ImageUtil.gauss_filter(original_img, sigma_value)
        threshold_img = ImageUtil.obtain_threshold_image(gauss_img)

        file_name = image_name + "_filter1_gauss_filter_para2_" + str(sigma_value) + ".tif"
        CommonUtil.save_image_to_folder(img=threshold_img, dir_path_str=output_dir, file_name=file_name)


        surface_area_list: list = ImageUtil.measure_surface_area_of_all_objects(threshold_img, original_img)
        surface_area_mean: float = CommonUtil.calc_mean(surface_area_list)
        surface_area_std_dev: float = CommonUtil.calc_standard_deviation(surface_area_list, surface_area_mean)

        perimeter_list: list = ImageUtil.measure_perimeter_of_all_objects(threshold_img, original_img)
        perimeter_mean: float = CommonUtil.calc_mean(perimeter_list)
        perimeter_std_dev: float = CommonUtil.calc_standard_deviation(perimeter_list, perimeter_mean)


        result_dict: dict = {}
        result_dict["image_name"] = image_name
        result_dict["filter_name"] = "gaussian"
        result_dict["parameter"] = "signma: " + str(sigma_value)

        result_dict["surface_area_list"] = str(surface_area_list)
        result_dict["surface_area_mean"] = surface_area_mean
        result_dict["surface_area_std_dev"] = surface_area_std_dev

        result_dict["perimeter_list"] = str(perimeter_list)
        result_dict["perimeter_mean"] = perimeter_mean
        result_dict["perimeter_std_dev"] = perimeter_std_dev

        result_dict_list.append(result_dict)



    # filter 2 para 1
    for image_name in image_name_list:
        original_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_diplib_image(image_name)

        median_para: str = 'rectangular'
        median_img = ImageUtil.median_filter(original_img, median_para)
        threshold_img = ImageUtil.obtain_threshold_image(median_img)

        file_name = image_name + "_filter1_median_filter_para1_" + str(median_para) + ".tif"
        CommonUtil.save_image_to_folder(img=threshold_img, dir_path_str=output_dir, file_name=file_name)


        surface_area_list: list = ImageUtil.measure_surface_area_of_all_objects(threshold_img, original_img)
        surface_area_mean: float = CommonUtil.calc_mean(surface_area_list)
        surface_area_std_dev: float = CommonUtil.calc_standard_deviation(surface_area_list, surface_area_mean)

        perimeter_list: list = ImageUtil.measure_perimeter_of_all_objects(threshold_img, original_img)
        perimeter_mean: float = CommonUtil.calc_mean(perimeter_list)
        perimeter_std_dev: float = CommonUtil.calc_standard_deviation(perimeter_list, perimeter_mean)


        result_dict: dict = {}
        result_dict["image_name"] = image_name
        result_dict["filter_name"] = "median"
        result_dict["parameter"] = median_para

        result_dict["surface_area_list"] = str(surface_area_list)
        result_dict["surface_area_mean"] = surface_area_mean
        result_dict["surface_area_std_dev"] = surface_area_std_dev

        result_dict["perimeter_list"] = str(perimeter_list)
        result_dict["perimeter_mean"] = perimeter_mean
        result_dict["perimeter_std_dev"] = perimeter_std_dev

        result_dict_list.append(result_dict)



    # filter 2 para 2
    for image_name in image_name_list:
        original_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_diplib_image(image_name)

        median_para: str = 'elliptic'
        median_img = ImageUtil.median_filter(original_img, median_para)
        threshold_img = ImageUtil.obtain_threshold_image(median_img)

        file_name = image_name + "_filter1_median_filter_para2_" + str(median_para) + ".tif"
        CommonUtil.save_image_to_folder(img=threshold_img, dir_path_str=output_dir, file_name=file_name)


        surface_area_list: list = ImageUtil.measure_surface_area_of_all_objects(threshold_img, original_img)
        surface_area_mean: float = CommonUtil.calc_mean(surface_area_list)
        surface_area_std_dev: float = CommonUtil.calc_standard_deviation(surface_area_list, surface_area_mean)

        perimeter_list: list = ImageUtil.measure_perimeter_of_all_objects(threshold_img, original_img)
        perimeter_mean: float = CommonUtil.calc_mean(perimeter_list)
        perimeter_std_dev: float = CommonUtil.calc_standard_deviation(perimeter_list, perimeter_mean)


        result_dict: dict = {}
        result_dict["image_name"] = image_name
        result_dict["filter_name"] = "median filter"
        result_dict["parameter"] = median_para

        result_dict["surface_area_list"] = str(surface_area_list)
        result_dict["surface_area_mean"] = surface_area_mean
        result_dict["surface_area_std_dev"] = surface_area_std_dev

        result_dict["perimeter_list"] = str(perimeter_list)
        result_dict["perimeter_mean"] = perimeter_mean
        result_dict["perimeter_std_dev"] = perimeter_std_dev

        result_dict_list.append(result_dict)




    CommonUtil.pretty_print(result_dict_list, width=1000)

    CommonUtil.press_enter_to_continue()
