import diplib
from diplib import PyDIPjavaio

from util.common_util import CommonUtil
from util.image_util import ImageUtil

# test_case
from util.plot_util import PlotUtil

if __name__ == '__main__':
    print("starting...")
    sleep_sec: int = 0

    image_name_list: list = ["AxioCamIm01_high_contrast"] #, "AxioCamIm02", "AxioCamIm03"]


    input_dir_str: str = CommonUtil.obtain_project_default_input_dir_path() + "asm3/"
    date_time_str: str = CommonUtil.generate_date_time_str()
    output_dir_str: str = CommonUtil.obtain_project_default_output_dir_path() + date_time_str + "/"
    CommonUtil.create_missing_dir(output_dir_str)


    shape_list = ['rectangular', 'elliptic', 'diamond', 'parabolic']
    se_length_list = [5,11,21,31,41,61,71,101]

    # filter 1 para 1
    for shape in shape_list:
        for se_length in se_length_list:
            for image_name in image_name_list:
                print(shape, se_length, image_name)

                original_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_image(image_name, input_dir_str);   #ImageUtil.show_image_in_dip_view(original_img, title="original img")
                CommonUtil.save_image_to_folder(original_img, output_dir_str, "original_img.tif")


                se_one_side_length: int = se_length #7
                se_shape: str = shape #"rectangular"

                # high_contrast_image = ImageUtil.increase_image_contrast(original_img)

                # obtain_pixel_value_list = ImageUtil.obtain_pixel_value_list(high_contrast_image)
                # plot_id: int = 1
                # plot_title: str = "t"
                # x_label: str = "x"
                # y_label: str = "y"
                # plot = PlotUtil.create_histogram_plot(plot_id, plot_title, x_label, y_label, obtain_pixel_value_list)
                # plot.pause(10)



                dilation_img = ImageUtil.dilation(original_img, se_one_side_length, se_shape)
                file_name = image_name + "_dil_img_" + shape + "_" + str(se_length) + ".tif"
                CommonUtil.save_image_to_folder(dilation_img, output_dir_str, file_name)

                closing_img = ImageUtil.closing(original_img, se_one_side_length, se_shape)
                file_name = image_name + "_closing_img_" + shape + "_" + str(se_length) + ".tif"
                CommonUtil.save_image_to_folder(closing_img, output_dir_str, file_name)

                invert_closing_img = ImageUtil.invert_img(closing_img)
                file_name = image_name + "_invert_closing_img_" + shape + "_" + str(se_length) + ".tif"
                CommonUtil.save_image_to_folder(invert_closing_img, output_dir_str, file_name)




                # invert_org_img = ImageUtil.invert_img(original_img)
                # file_name = image_name + "_invert_org_img_" + shape + "_" + str(se_length) + ".tif"
                # CommonUtil.save_image_to_folder(invert_org_img, output_dir_str, file_name)

                #
                # erosion_img = ImageUtil.erosion(high_contrast_image, se_one_side_length, se_shape)
                # file_name = image_name + "_ero_img_" + shape + "_" + str(se_length) + ".tif"
                # CommonUtil.save_image_to_folder(erosion_img, output_dir_str, file_name)

                #
                # closing_img = ImageUtil.erosion(dilation_img, se_one_side_length, se_shape)
                # file_name = image_name + "_closing_img_" + shape + "_" + str(se_length) + ".tif"
                # CommonUtil.save_image_to_folder(closing_img, output_dir_str, file_name)
                #
                #
                #
                # black_hat_img = ImageUtil.subtraction_img1_minus_img2(white_img, high_contrast_image);        #ImageUtil.show_image_in_dip_view(original_img, title="original img")
                # file_name = image_name + "_black_hat_img_" + shape + "_" + str(se_length) + ".tif"
                # CommonUtil.save_image_to_folder(black_hat_img, output_dir_str, file_name)




                # inverted_img = ImageUtil.invert_img(original_img);
                # CommonUtil.save_image_to_folder(inverted_img, output_dir_str, "inverted_img.tif")
                #
                #
                # white_hat_img = ImageUtil.top_hat(inverted_img, se_one_side_length, se_shape)
                # file_name = image_name + "_white_hat_img_" + shape + "_" + str(se_length) + ".tif"
                # CommonUtil.save_image_to_folder(white_hat_img, output_dir_str, file_name)
                #
                # white_hat_threshold_img = diplib.Threshold(white_hat_img)[0]
                # file_name = image_name + "_white_hat_threshold_img_" + shape + "_" + str(se_length) + ".tif"
                # CommonUtil.save_image_to_folder(white_hat_threshold_img, output_dir_str, file_name)



                # closing_img = ImageUtil.closing(inverted_img, se_one_side_length, se_shape)
                # file_name = image_name + "_closing_img_" + shape + "_" + str(se_length) + ".tif"
                # CommonUtil.save_image_to_folder(closing_img, output_dir_str, file_name)

                # black_hat_img = ImageUtil.top_hat(inverted_img, se_one_side_length, se_shape);   #ImageUtil.show_image_in_dip_view(black_hat_img, title="black_hat_img")
                # file_name = image_name + "_" + shape + "_" + str(se_length) + ".tif"
                # CommonUtil.save_image_to_folder(black_hat_img, output_dir_str, file_name)



                # filtered_img = ImageUtil.median_filter(original_img, "rectangular");   #ImageUtil.show_image_in_dip_view(filtered_img, title="filtered_img")





                # threshold_img = ImageUtil.obtain_threshold_image(filtered_img);     #ImageUtil.show_image_in_dip_view(threshold_img, title="threshold_img")
                # CommonUtil.save_image_to_folder(threshold_img, output_dir_str, "threshold_img.tif")
                #
                #

                # # erosion_img = ImageUtil.erosion(threshold_img, se_one_side_length, se_shape);     ImageUtil.show_image_in_dip_view(erosion_img, title="erosion_img")
                # # erosion_img2 = ImageUtil.erosion(erosion_img, se_one_side_length, se_shape);     ImageUtil.show_image_in_dip_view(erosion_img2, title="erosion_img2")
                #
                # # dilation_img = ImageUtil.dilation(threshold_img, se_one_side_length, se_shape);     ImageUtil.show_image_in_dip_view(dilation_img, title="dilation_img")
                # # opening_img = ImageUtil.opening(threshold_img, se_one_side_length, se_shape);     ImageUtil.show_image_in_dip_view(opening_img, title="opening_img")
                # # # opening_img = ImageUtil.opening(opening_img, se_one_side_length, se_shape);     ImageUtil.show_image_in_dip_view(opening_img, title="opening_img2")
                # # closing_img = ImageUtil.closing(threshold_img, se_one_side_length, se_shape);     #ImageUtil.show_image_in_dip_view(closing_img, title="closing_img")
                #
                # black_hat_img = ImageUtil.top_hat(original_img, se_one_side_length, se_shape);   #ImageUtil.show_image_in_dip_view(black_hat_img, title="black_hat_img")
                # file_name = image_name + "_" + shape + "_" + str(se_length) + ".tif"
                # CommonUtil.save_image_to_folder(black_hat_img, output_dir_str, file_name)
                #
                #
                # # file_name = image_name + "_filter1_gauss_filter_para1_" + str(sigma_value) + ".tif"
                # # CommonUtil.save_image_to_default_project_folder(img=original_img, dir_name=date_time_str, file_name=file_name)





    print("output_dir_str", output_dir_str)
    CommonUtil.press_enter_to_continue()


    CommonUtil.press_enter_to_continue()
