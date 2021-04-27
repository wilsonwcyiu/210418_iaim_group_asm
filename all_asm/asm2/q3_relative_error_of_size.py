from diplib import PyDIPjavaio
from matplotlib import pyplot

from util.common_util import CommonUtil
from util.image_util import ImageUtil


# test_case
from util.plot_util import PlotUtil

if __name__ == '__main__':
    print("starting...")
    sleep_sec: int = 0

    image_name_list: list = ["rect1", "rect2", "rect3", "rect4"]

    xy_tuple_list: list = []

    date_time_str: str = CommonUtil.generate_date_time_str()
    for image_name in image_name_list:
        original_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_image(image_name)
        threshold_img = ImageUtil.obtain_threshold_image(original_img)

        surface_area_list: list = ImageUtil.measure_surface_area_of_all_objects(threshold_img, original_img)
        mean: float = CommonUtil.calc_mean(surface_area_list)
        std_dev: float = CommonUtil.calc_standard_deviation(surface_area_list, mean)

        square_root_of_area_mean: float = CommonUtil.square_root(mean)
        coefficient_of_variation: float = std_dev / mean
        xy_tuple_list.append((square_root_of_area_mean, coefficient_of_variation))

        print("image_name", image_name, "\t",
              "mean", mean, "\t",
              "std_dev", std_dev, "\t",
              "square_root_of_area_mean", square_root_of_area_mean, "\t",
              "coefficient_of_variation", coefficient_of_variation
              )


    xy_tuple_list.sort()
    plot_id: int = 1
    plot_title: str = "Relative Error of size"
    x_label: str = "Square root of Area Mean"
    y_label: str = "Coefficient of Variation (CV)"
    plt: pyplot = PlotUtil.create_plot(plot_id, plot_title, x_label, y_label, xy_tuple_list)

    plt.pause(10)
    file_name: str = "Relative Error of size"
    date_time_str: str = CommonUtil.generate_date_time_str()
    PlotUtil.save_plot_to_project_folder(plt, date_time_str, file_name)