import diplib
from diplib import PyDIPjavaio

from util.common_util import CommonUtil
from util.image_util import ImageUtil

# test_case
from util.plot_util import PlotUtil

if __name__ == '__main__':
    print("starting...")
    sleep_sec: int = 0

    # image_name_list: list = ["AxioCamIm01_high_contrast", "AxioCamIm02_high_contrast", "AxioCamIm03_high_contrast"]
    # image_name_list.append("AxioCamIm01_high_contrast_black_hat_img_diamond_51")


    input_dir_str: str = CommonUtil.obtain_project_default_input_dir_path() + "asm3/"
    date_time_str: str = CommonUtil.generate_date_time_str()
    output_dir_str: str = CommonUtil.obtain_project_default_output_dir_path() + date_time_str + "/"
    CommonUtil.create_missing_dir(output_dir_str)


    shape_list = ['elliptic'] #'diamond', 'parabolic', 'rectangular']
    se_length_list = [71]

    image_name: str = "AxioCamIm01_high_contrast"
    for shape in shape_list:
        for se_length in se_length_list:
            print(shape, se_length, image_name)

            high_contrast_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_image(image_name, input_dir_str);   #ImageUtil.show_image_in_dip_view(high_contrast_img, title="high_contrast_img")
            CommonUtil.save_image_to_folder(high_contrast_img, output_dir_str, image_name + "_original_img.tif")

            se_one_side_length: int = se_length
            se_shape: str = shape

            closing_img = ImageUtil.closing(high_contrast_img, se_one_side_length, se_shape)
            file_name = image_name + "_closing_img_" + shape + "_" + str(se_length) + ".tif"
            CommonUtil.save_image_to_folder(closing_img, output_dir_str, file_name)


            black_hat_img = ImageUtil.black_hat(high_contrast_img, se_one_side_length, se_shape)
            file_name = image_name + "_black_hat_icmg_" + shape + "_" + str(se_length) + ".tif"
            CommonUtil.save_image_to_folder(black_hat_img, output_dir_str, file_name)

            # ImageUtil.show_image_in_dip_view(black_hat_img, title=image_name)

            threshold_img = ImageUtil.obtain_threshold_image(black_hat_img);            ImageUtil.show_image_in_dip_view(threshold_img, title=image_name + "_threshold_img")


            # obtain_pixel_value_list = ImageUtil.obtain_pixel_value_list(black_hat_img);
            # plot_id: int = 1; plot_title: str = "t"; x_label: str = "x"; y_label: str = "y"
            # plot = PlotUtil.create_histogram_plot(plot_id, plot_title, x_label, y_label, obtain_pixel_value_list)
            # plot.show()



    shape_list = ['elliptic'] #'diamond', 'parabolic', 'rectangular']
    se_length_list = [91]

    image_name: str = "AxioCamIm02_high_contrast"
    for shape in shape_list:
        for se_length in se_length_list:
            print(shape, se_length, image_name)

            high_contrast_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_image(image_name, input_dir_str);   #ImageUtil.show_image_in_dip_view(high_contrast_img, title="high_contrast_img")
            CommonUtil.save_image_to_folder(high_contrast_img, output_dir_str, image_name + "_original_img.tif")


            se_one_side_length: int = se_length
            se_shape: str = shape

            closing_img = ImageUtil.closing(high_contrast_img, se_one_side_length, se_shape)
            file_name = image_name + "_closing_img_" + shape + "_" + str(se_length) + ".tif"
            CommonUtil.save_image_to_folder(closing_img, output_dir_str, file_name)


            black_hat_img = ImageUtil.black_hat(high_contrast_img, se_one_side_length, se_shape)
            file_name = image_name + "_black_hat_icmg_" + shape + "_" + str(se_length) + ".tif"
            CommonUtil.save_image_to_folder(black_hat_img, output_dir_str, file_name)

            # ImageUtil.show_image_in_dip_view(black_hat_img, title=image_name)

            threshold_img = ImageUtil.obtain_threshold_image(black_hat_img);            ImageUtil.show_image_in_dip_view(threshold_img, title=image_name + "_threshold_img")

            # obtain_pixel_value_list = ImageUtil.obtain_pixel_value_list(black_hat_img);
            # plot_id: int = 1; plot_title: str = "t"; x_label: str = "x"; y_label: str = "y"
            # plot = PlotUtil.create_histogram_plot(plot_id, plot_title, x_label, y_label, obtain_pixel_value_list)
            # plot.show()



    shape_list = ['elliptic'] #'diamond', 'parabolic', 'rectangular']
    se_length_list = [181]

    image_name: str = "AxioCamIm03_high_contrast"
    for shape in shape_list:
        for se_length in se_length_list:
            print(shape, se_length, image_name)

            high_contrast_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_image(image_name, input_dir_str);   #ImageUtil.show_image_in_dip_view(high_contrast_img, title="high_contrast_img")
            CommonUtil.save_image_to_folder(high_contrast_img, output_dir_str, image_name + "_original_img.tif")


            se_one_side_length: int = se_length
            se_shape: str = shape

            closing_img = ImageUtil.closing(high_contrast_img, se_one_side_length, se_shape)
            file_name = image_name + "_closing_img_" + shape + "_" + str(se_length) + ".tif"
            CommonUtil.save_image_to_folder(closing_img, output_dir_str, file_name)


            black_hat_img = ImageUtil.black_hat(high_contrast_img, se_one_side_length, se_shape)
            file_name = image_name + "_black_hat_icmg_" + shape + "_" + str(se_length) + ".tif"
            CommonUtil.save_image_to_folder(black_hat_img, output_dir_str, file_name)

            # ImageUtil.show_image_in_dip_view(black_hat_img, title=image_name)
            median_img = ImageUtil.median_filter(black_hat_img, 60)
            threshold_img = ImageUtil.obtain_threshold_image(median_img);            ImageUtil.show_image_in_dip_view(threshold_img, title=image_name + "_median_threshold_img")

            # obtain_pixel_value_list = ImageUtil.obtain_pixel_value_list(black_hat_img);
            # plot_id: int = 1; plot_title: str = "t"; x_label: str = "x"; y_label: str = "y"
            # plot = PlotUtil.create_histogram_plot(plot_id, plot_title, x_label, y_label, obtain_pixel_value_list)
            # plot.show()


    print("output_dir_str", output_dir_str)
    CommonUtil.press_enter_to_continue()


    CommonUtil.press_enter_to_continue()
