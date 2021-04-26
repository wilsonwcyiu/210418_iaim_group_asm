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


    date_time_str: str = CommonUtil.generate_date_time_str()
    output_dir: str = CommonUtil.obtain_project_default_output_dir_path() + date_time_str + "/"

    # image_name_list: list = ["rect1", "rect2", "rect3", "rect4"]
    # img_file_group_name_id: str = "_imgOrg"

    image_name_list: list = ["rect1a", "rect2a", "rect3a", "rect4a"]
    img_file_group_name_id: str = "_imgA"

    # image_name_list: list = ["rect1b", "rect2b", "rect3b", "rect4b"]
    # img_file_group_name_id: str = "_imgB"

    smallest_object_size: int = 200
    # smallest_object_perimeter: int = 100


    surface_area_relative_error_xy_tuple_list: list = []
    perimeter_relative_error_xy_tuple_list: list = []

    # filter 1 para 1
    print("gauss, sigma_value: 2")
    for image_name in image_name_list:
        # filter image
        original_image: PyDIPjavaio.ImageRead = ImageUtil.obtain_image(image_name)

        sigma_value: int = 2
        original_image: diplib.PyDIP_bin.Image = ImageUtil.gauss_filter(original_image, sigma_value)
        threshold_img = ImageUtil.obtain_threshold_image(original_image)

        file_name = image_name + "_filter1_gauss_filter_para1_" + str(sigma_value) + ".tif"
        CommonUtil.save_image_to_folder(img=threshold_img, dir_path_str=output_dir, file_name=file_name)


        # surface relative error
        surface_area_list: list = ImageUtil.measure_surface_area_of_all_objects(threshold_img, original_image)
        surface_area_list = [x for x in surface_area_list if x > smallest_object_size]
        print("image ", image_name, " detected image(surface_area_list) ", len(surface_area_list), "\t", surface_area_list)

        (square_root_of_area_mean, coefficient_of_variation) = CommonUtil.derive_relative_error(surface_area_list)
        surface_area_relative_error_xy_tuple_list.append((square_root_of_area_mean, coefficient_of_variation))
        surface_area_relative_error_xy_tuple_list.sort()


        # perimeter relative error
        perimeter_list: list = ImageUtil.measure_perimeter_of_all_objects(threshold_img, original_image)

        perimeter_list.sort(reverse=True)
        perimeter_list = perimeter_list[:len(surface_area_list)]

        print("image ", image_name, " detected image(perimeter_list) ", len(perimeter_list), "\t", perimeter_list)

        (square_root_of_perimeter_mean, coefficient_of_variation) = CommonUtil.derive_relative_error(perimeter_list)
        perimeter_relative_error_xy_tuple_list.append((square_root_of_perimeter_mean, coefficient_of_variation))
        perimeter_relative_error_xy_tuple_list.sort()


    plot_id: int = 1; plot_title: str = "Relative Error";  x_label: str = "Square root of Size Mean";  y_label: str = "Coefficient of Variation (CV)"
    plt: pyplot = PlotUtil.create_plot(plot_id, plot_title, x_label, y_label, surface_area_relative_error_xy_tuple_list, marker="o")

    plot_file_name: str = "relative_error_of" + img_file_group_name_id + "_size_filter1_gauss_filter_para1_" + str(sigma_value)
    PlotUtil.save_plot_to_folder(plt, output_dir, plot_file_name)


    plot_id: int = 2; plot_title: str = "Relative Error";  x_label: str = "Square root of Perimeter Mean";  y_label: str = "Coefficient of Variation (CV)"
    plt: pyplot = PlotUtil.create_plot(plot_id, plot_title, x_label, y_label, perimeter_relative_error_xy_tuple_list, marker="o")

    plot_file_name: str = "relative_error_of" + img_file_group_name_id + "_perimeter_filter1_gauss_filter_para1_" + str(sigma_value)
    PlotUtil.save_plot_to_folder(plt, output_dir, plot_file_name)
    print("\n")


    surface_area_relative_error_xy_tuple_list: list = []
    perimeter_relative_error_xy_tuple_list: list = []

    # filter 1 para 2
    print("gauss, sigma_value: 3")
    for image_name in image_name_list:
        # filter image
        original_image: PyDIPjavaio.ImageRead = ImageUtil.obtain_image(image_name)

        sigma_value: int = 3
        original_image: diplib.PyDIP_bin.Image = ImageUtil.gauss_filter(original_image, sigma_value)
        threshold_img = ImageUtil.obtain_threshold_image(original_image)

        file_name = image_name + "_filter1_gauss_filter_para2_" + str(sigma_value) + ".tif"
        CommonUtil.save_image_to_folder(img=threshold_img, dir_path_str=output_dir, file_name=file_name)


        # surface relative error
        surface_area_list: list = ImageUtil.measure_surface_area_of_all_objects(threshold_img, original_image)
        surface_area_list = [x for x in surface_area_list if x > smallest_object_size]
        print("image ", image_name, " detected image(surface_area_list) ", len(surface_area_list), "\t", surface_area_list)

        (square_root_of_area_mean, coefficient_of_variation) = CommonUtil.derive_relative_error(surface_area_list)
        surface_area_relative_error_xy_tuple_list.append((square_root_of_area_mean, coefficient_of_variation))
        surface_area_relative_error_xy_tuple_list.sort()


        # perimeter relative error
        perimeter_list: list = ImageUtil.measure_perimeter_of_all_objects(threshold_img, original_image)

        perimeter_list.sort(reverse=True)
        perimeter_list = perimeter_list[:len(surface_area_list)]

        print("image ", image_name, " detected image(perimeter_list) ", len(perimeter_list), "\t", perimeter_list)

        (square_root_of_perimeter_mean, coefficient_of_variation) = CommonUtil.derive_relative_error(perimeter_list)
        perimeter_relative_error_xy_tuple_list.append((square_root_of_perimeter_mean, coefficient_of_variation))
        perimeter_relative_error_xy_tuple_list.sort()


    plot_id: int = 3; plot_title: str = "Relative Error";  x_label: str = "Square root of Size Mean";  y_label: str = "Coefficient of Variation (CV)"
    plt: pyplot = PlotUtil.create_plot(plot_id, plot_title, x_label, y_label, surface_area_relative_error_xy_tuple_list, marker="o")

    plot_file_name: str = "relative_error_of" + img_file_group_name_id + "_size_filter1_gauss_filter_para2_" + str(sigma_value)
    PlotUtil.save_plot_to_project_folder(plt, date_time_str, plot_file_name)


    plot_id: int = 4; plot_title: str = "Relative Error";  x_label: str = "Square root of Perimeter Mean";  y_label: str = "Coefficient of Variation (CV)"
    plt: pyplot = PlotUtil.create_plot(plot_id, plot_title, x_label, y_label, perimeter_relative_error_xy_tuple_list, marker="o")

    plot_file_name: str = "relative_error_of" + img_file_group_name_id + "_perimeter_filter1_gauss_filter_para2_" + str(sigma_value)
    PlotUtil.save_plot_to_project_folder(plt, date_time_str, plot_file_name)
    print("\n")


    surface_area_relative_error_xy_tuple_list: list = []
    perimeter_relative_error_xy_tuple_list: list = []

    # filter 2 para 1
    print("median, para: rectangular")
    for image_name in image_name_list:
        # filter image
        original_image: PyDIPjavaio.ImageRead = ImageUtil.obtain_image(image_name)

        median_para: str = 'rectangular'
        median_img = ImageUtil.median_filter(original_image, median_para)

        threshold_img = ImageUtil.obtain_threshold_image(median_img)

        file_name = image_name + "_filter2_median_filter_para1_" + str(median_para) + ".tif"
        CommonUtil.save_image_to_folder(img=threshold_img, dir_path_str=output_dir, file_name=file_name)


        # surface relative error
        surface_area_list: list = ImageUtil.measure_surface_area_of_all_objects(threshold_img, original_image)
        surface_area_list = [x for x in surface_area_list if x > smallest_object_size]
        print("image ", image_name, " detected image(surface_area_list) ", len(surface_area_list), "\t", surface_area_list)

        (square_root_of_area_mean, coefficient_of_variation) = CommonUtil.derive_relative_error(surface_area_list)
        surface_area_relative_error_xy_tuple_list.append((square_root_of_area_mean, coefficient_of_variation))
        surface_area_relative_error_xy_tuple_list.sort()


        # perimeter relative error
        perimeter_list: list = ImageUtil.measure_perimeter_of_all_objects(threshold_img, original_image)

        perimeter_list.sort(reverse=True)
        perimeter_list = perimeter_list[:len(surface_area_list)]

        print("image ", image_name, " detected image(perimeter_list) ", len(perimeter_list), "\t", perimeter_list)

        (square_root_of_perimeter_mean, coefficient_of_variation) = CommonUtil.derive_relative_error(perimeter_list)
        perimeter_relative_error_xy_tuple_list.append((square_root_of_perimeter_mean, coefficient_of_variation))
        perimeter_relative_error_xy_tuple_list.sort()


    plot_id: int = 5; plot_title: str = "Relative Error";  x_label: str = "Square root of Size Mean";  y_label: str = "Coefficient of Variation (CV)"
    plt: pyplot = PlotUtil.create_plot(plot_id, plot_title, x_label, y_label, surface_area_relative_error_xy_tuple_list, marker="o")

    plot_file_name: str = "relative_error_of" + img_file_group_name_id + "_size_filter2_median_filter_para1_" + str(median_para)
    PlotUtil.save_plot_to_project_folder(plt, date_time_str, plot_file_name)


    plot_id: int = 6; plot_title: str = "Relative Error";  x_label: str = "Square root of Perimeter Mean";  y_label: str = "Coefficient of Variation (CV)"
    plt: pyplot = PlotUtil.create_plot(plot_id, plot_title, x_label, y_label, perimeter_relative_error_xy_tuple_list, marker="o")

    plot_file_name: str = "relative_error_of" + img_file_group_name_id + "_perimeter_filter2_median_filter_para1_" + str(median_para)
    PlotUtil.save_plot_to_project_folder(plt, date_time_str, plot_file_name)
    print("\n")


    surface_area_relative_error_xy_tuple_list: list = []
    perimeter_relative_error_xy_tuple_list: list = []

    # filter 2 para 2
    print("median, para: elliptic")
    for image_name in image_name_list:
        # filter image
        original_image: PyDIPjavaio.ImageRead = ImageUtil.obtain_image(image_name)

        median_para: str = 'elliptic'
        median_img = ImageUtil.median_filter(original_image, median_para)

        threshold_img = ImageUtil.obtain_threshold_image(median_img)

        file_name = image_name + "_filter2_median_filter_para2_" + str(median_para) + ".tif"
        CommonUtil.save_image_to_folder(img=threshold_img, dir_path_str=output_dir, file_name=file_name)


        # surface relative error
        surface_area_list: list = ImageUtil.measure_surface_area_of_all_objects(threshold_img, original_image)
        surface_area_list = [x for x in surface_area_list if x > smallest_object_size]
        print("image ", image_name, " detected image(surface_area_list) ", len(surface_area_list), "\t", surface_area_list)

        (square_root_of_area_mean, coefficient_of_variation) = CommonUtil.derive_relative_error(surface_area_list)
        surface_area_relative_error_xy_tuple_list.append((square_root_of_area_mean, coefficient_of_variation))
        surface_area_relative_error_xy_tuple_list.sort()


        # perimeter relative error
        perimeter_list: list = ImageUtil.measure_perimeter_of_all_objects(threshold_img, original_image)

        perimeter_list.sort(reverse=True)
        perimeter_list = perimeter_list[:len(surface_area_list)]

        print("image ", image_name, " detected image(perimeter_list) ", len(perimeter_list), "\t", perimeter_list)

        (square_root_of_perimeter_mean, coefficient_of_variation) = CommonUtil.derive_relative_error(perimeter_list)
        perimeter_relative_error_xy_tuple_list.append((square_root_of_perimeter_mean, coefficient_of_variation))
        perimeter_relative_error_xy_tuple_list.sort()


    plot_id: int = 7; plot_title: str = "Relative Error";  x_label: str = "Square root of Size Mean";  y_label: str = "Coefficient of Variation (CV)"
    plt: pyplot = PlotUtil.create_plot(plot_id, plot_title, x_label, y_label, surface_area_relative_error_xy_tuple_list, marker="o")

    plot_file_name: str = "relative_error_of" + img_file_group_name_id + "_size_filter2_median_filter_para2_" + str(median_para)
    PlotUtil.save_plot_to_folder(plt, output_dir, plot_file_name)


    plot_id: int = 8; plot_title: str = "The relative discretization error of perimeter";  x_label: str = "square root of the mean";  y_label: str = "coefficient of variation"
    plt: pyplot = PlotUtil.create_plot(plot_id, plot_title, x_label, y_label, perimeter_relative_error_xy_tuple_list, marker="")

    plot_file_name: str = "relative_error_of" + img_file_group_name_id + "_perimeter_filter2_median_filter_para2_" + str(median_para)
    PlotUtil.save_plot_to_folder(plt, output_dir, plot_file_name)




    CommonUtil.press_enter_to_continue()
