import diplib
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


    surface_area_relative_error_xy_tuple_list: list = []
    perimeter_relative_error_xy_tuple_list: list = []
    # filter 1 para 1
    for image_name in image_name_list:
        # filter image
        original_image: PyDIPjavaio.ImageRead = ImageUtil.obtain_image(image_name)

        sigma_value: int = 2
        original_image: diplib.PyDIP_bin.Image = ImageUtil.gauss_filter(original_image, sigma_value)
        threshold_image = ImageUtil.obtain_threshold_image(original_image)

        file_name = image_name + "_filter1_gauss_filter_para1_" + str(sigma_value) + ".tif"
        CommonUtil.save_image_to_default_project_folder(img=threshold_image, dir_name=date_time_str, file_name=file_name)


        # surface relative error
        surface_area_list: list = ImageUtil.measure_surface_area_of_all_objects(threshold_image, original_image)
        (square_root_of_area_mean, coefficient_of_variation) = CommonUtil.derive_relative_error(surface_area_list)
        surface_area_relative_error_xy_tuple_list.append((square_root_of_area_mean, coefficient_of_variation))
        surface_area_relative_error_xy_tuple_list.sort()


        # perimeter relative error
        perimeter_list: list = ImageUtil.measure_perimeter_of_all_objects(threshold_image, original_image)
        (square_root_of_perimeter_mean, coefficient_of_variation) = CommonUtil.derive_relative_error(perimeter_list)

        perimeter_relative_error_xy_tuple_list.append((square_root_of_perimeter_mean, coefficient_of_variation))
        perimeter_relative_error_xy_tuple_list.sort()


    plot_id: int = 1; plot_title: str = "Relative Error";  x_label: str = "Square root of Size Mean";  y_label: str = "Coefficient of Variation (CV)"
    plt: pyplot = PlotUtil.create_plot(plot_id, plot_title, x_label, y_label, surface_area_relative_error_xy_tuple_list)

    plot_file_name: str = "relative_error_of_size_filter1_gauss_filter_para1_" + str(sigma_value)
    PlotUtil.save_plot_to_project_folder(plt, date_time_str, plot_file_name)


    plot_id: int = 2; plot_title: str = "Relative Error";  x_label: str = "Square root of Perimeter Mean";  y_label: str = "Coefficient of Variation (CV)"
    plt: pyplot = PlotUtil.create_plot(plot_id, plot_title, x_label, y_label, perimeter_relative_error_xy_tuple_list)

    plot_file_name: str = "relative_error_of_perimeter_filter1_gauss_filter_para1_" + str(sigma_value)
    PlotUtil.save_plot_to_project_folder(plt, date_time_str, plot_file_name)




    # filter 1 para 2
    for image_name in image_name_list:
        # filter image
        original_image: PyDIPjavaio.ImageRead = ImageUtil.obtain_image(image_name)

        sigma_value: int = 3
        original_image: diplib.PyDIP_bin.Image = ImageUtil.gauss_filter(original_image, sigma_value)
        threshold_image = ImageUtil.obtain_threshold_image(original_image)

        file_name = image_name + "_filter1_gauss_filter_para2_" + str(sigma_value) + ".tif"
        CommonUtil.save_image_to_default_project_folder(img=threshold_image, dir_name=date_time_str, file_name=file_name)


        # surface relative error
        surface_area_list: list = ImageUtil.measure_surface_area_of_all_objects(threshold_image, original_image)
        (square_root_of_area_mean, coefficient_of_variation) = CommonUtil.derive_relative_error(surface_area_list)
        surface_area_relative_error_xy_tuple_list.append((square_root_of_area_mean, coefficient_of_variation))
        surface_area_relative_error_xy_tuple_list.sort()


        # perimeter relative error
        perimeter_list: list = ImageUtil.measure_perimeter_of_all_objects(threshold_image, original_image)
        (square_root_of_perimeter_mean, coefficient_of_variation) = CommonUtil.derive_relative_error(perimeter_list)

        perimeter_relative_error_xy_tuple_list.append((square_root_of_perimeter_mean, coefficient_of_variation))
        perimeter_relative_error_xy_tuple_list.sort()


    plot_id: int = 3; plot_title: str = "Relative Error";  x_label: str = "Square root of Size Mean";  y_label: str = "Coefficient of Variation (CV)"
    plt: pyplot = PlotUtil.create_plot(plot_id, plot_title, x_label, y_label, surface_area_relative_error_xy_tuple_list)

    plot_file_name: str = "relative_error_of_size_filter1_gauss_filter_para2_" + str(sigma_value)
    PlotUtil.save_plot_to_project_folder(plt, date_time_str, plot_file_name)


    plot_id: int = 4; plot_title: str = "Relative Error";  x_label: str = "Square root of Perimeter Mean";  y_label: str = "Coefficient of Variation (CV)"
    plt: pyplot = PlotUtil.create_plot(plot_id, plot_title, x_label, y_label, perimeter_relative_error_xy_tuple_list)

    plot_file_name: str = "relative_error_of_perimeter_filter1_gauss_filter_para2_" + str(sigma_value)
    PlotUtil.save_plot_to_project_folder(plt, date_time_str, plot_file_name)




    # filter 2 para 1
    for image_name in image_name_list:
        # filter image
        original_image: PyDIPjavaio.ImageRead = ImageUtil.obtain_image(image_name)

        median_para: str = 'rectangular'
        median_img = ImageUtil.median_filter(original_image, median_para)

        threshold_img = ImageUtil.obtain_threshold_image(median_img)

        file_name = image_name + "_filter2_median_filter_para1_" + str(sigma_value) + ".tif"
        CommonUtil.save_image_to_default_project_folder(img=threshold_image, dir_name=date_time_str, file_name=file_name)


        # surface relative error
        surface_area_list: list = ImageUtil.measure_surface_area_of_all_objects(threshold_image, original_image)
        (square_root_of_area_mean, coefficient_of_variation) = CommonUtil.derive_relative_error(surface_area_list)
        surface_area_relative_error_xy_tuple_list.append((square_root_of_area_mean, coefficient_of_variation))
        surface_area_relative_error_xy_tuple_list.sort()


        # perimeter relative error
        perimeter_list: list = ImageUtil.measure_perimeter_of_all_objects(threshold_image, original_image)
        (square_root_of_perimeter_mean, coefficient_of_variation) = CommonUtil.derive_relative_error(perimeter_list)

        perimeter_relative_error_xy_tuple_list.append((square_root_of_perimeter_mean, coefficient_of_variation))
        perimeter_relative_error_xy_tuple_list.sort()


    plot_id: int = 5; plot_title: str = "Relative Error";  x_label: str = "Square root of Size Mean";  y_label: str = "Coefficient of Variation (CV)"
    plt: pyplot = PlotUtil.create_plot(plot_id, plot_title, x_label, y_label, surface_area_relative_error_xy_tuple_list)

    plot_file_name: str = "relative_error_of_size_filter2_median_filter_para1_" + str(sigma_value)
    PlotUtil.save_plot_to_project_folder(plt, date_time_str, plot_file_name)


    plot_id: int = 6; plot_title: str = "Relative Error";  x_label: str = "Square root of Perimeter Mean";  y_label: str = "Coefficient of Variation (CV)"
    plt: pyplot = PlotUtil.create_plot(plot_id, plot_title, x_label, y_label, perimeter_relative_error_xy_tuple_list)

    plot_file_name: str = "relative_error_of_perimeter_filter2_median_filter_para1_" + str(sigma_value)
    PlotUtil.save_plot_to_project_folder(plt, date_time_str, plot_file_name)




    # filter 2 para 2
    for image_name in image_name_list:
        # filter image
        original_image: PyDIPjavaio.ImageRead = ImageUtil.obtain_image(image_name)

        median_para: str = 'elliptic'
        median_img = ImageUtil.median_filter(original_image, median_para)

        threshold_img = ImageUtil.obtain_threshold_image(median_img)

        file_name = image_name + "_filter2_median_filter_para2_" + str(sigma_value) + ".tif"
        CommonUtil.save_image_to_default_project_folder(img=threshold_image, dir_name=date_time_str, file_name=file_name)


        # surface relative error
        surface_area_list: list = ImageUtil.measure_surface_area_of_all_objects(threshold_image, original_image)
        (square_root_of_area_mean, coefficient_of_variation) = CommonUtil.derive_relative_error(surface_area_list)
        surface_area_relative_error_xy_tuple_list.append((square_root_of_area_mean, coefficient_of_variation))
        surface_area_relative_error_xy_tuple_list.sort()


        # perimeter relative error
        perimeter_list: list = ImageUtil.measure_perimeter_of_all_objects(threshold_image, original_image)
        (square_root_of_perimeter_mean, coefficient_of_variation) = CommonUtil.derive_relative_error(perimeter_list)

        perimeter_relative_error_xy_tuple_list.append((square_root_of_perimeter_mean, coefficient_of_variation))
        perimeter_relative_error_xy_tuple_list.sort()


    plot_id: int = 7; plot_title: str = "Relative Error";  x_label: str = "Square root of Size Mean";  y_label: str = "Coefficient of Variation (CV)"
    plt: pyplot = PlotUtil.create_plot(plot_id, plot_title, x_label, y_label, surface_area_relative_error_xy_tuple_list)

    plot_file_name: str = "relative_error_of_size_filter2_median_filter_para2_" + str(sigma_value)
    PlotUtil.save_plot_to_project_folder(plt, date_time_str, plot_file_name)


    plot_id: int = 8; plot_title: str = "Relative Error";  x_label: str = "Square root of Perimeter Mean";  y_label: str = "Coefficient of Variation (CV)"
    plt: pyplot = PlotUtil.create_plot(plot_id, plot_title, x_label, y_label, perimeter_relative_error_xy_tuple_list)

    plot_file_name: str = "relative_error_of_perimeter_filter2_median_filter_para2_" + str(sigma_value)
    PlotUtil.save_plot_to_project_folder(plt, date_time_str, plot_file_name)




    CommonUtil.press_enter_to_continue()

    #     perimeter_list: list = ImageUtil.measure_perimeter_of_all_objects(tmp_img)
    #     mean: float = CommonUtil.calc_mean(perimeter_list)
    #     std_dev: float = CommonUtil.calc_standard_deviation(perimeter_list, mean)
    #
    #     square_root_of_perimeter_mean: float = CommonUtil.square_root(mean)
    #     coefficient_of_variation: float = std_dev / mean
    #     xy_tuple_list.append((square_root_of_perimeter_mean, coefficient_of_variation))
    #
    #     print("image_name", image_name, "\t",
    #           "mean", mean, "\t",
    #           "std_dev", std_dev, "\t",
    #           "square_root_of_perimeter_mean", square_root_of_perimeter_mean, "\t",
    #           "coefficient_of_variation", coefficient_of_variation
    #           )
    #
    #
    # xy_tuple_list.sort()
    # plot_id: int = 1
    # plot_title: str = "Relative Error"
    # x_label: str = "Square root of Perimeter Mean"
    # y_label: str = "Coefficient of Variation (CV)"
    # plt: pyplot = PlotUtil.create_plot(plot_id, plot_title, x_label, y_label, xy_tuple_list)
    #
    # plt.pause(10)
    # file_name: str = "Relative Error"
    # date_time_str: str = CommonUtil.generate_date_time_str()
    # PlotUtil.save_plot_to_project_folder(plt, date_time_str, file_name)