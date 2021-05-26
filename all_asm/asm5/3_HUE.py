# (2) Compute the average hue feature all berries in the images.
import PIL
import diplib
from diplib import PyDIPjavaio

from util.common_util import CommonUtil
from util.image_util import ImageUtil
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
#importing required libraries
from skimage.io import imread
from skimage.transform import resize
from skimage.feature import hog

from skimage import data
import matplotlib.pyplot as plt

from util.plot_util import PlotUtil


# https://www.programmersought.com/article/54406295171/
if __name__ == '__main__':

    # Configure files and directories
    input_dir: str = CommonUtil.obtain_project_default_input_dir_path() + 'asm5/'
    proj_output_dir_path: str = '../../image_output/'
    img_extension: str = ""


    folder_list: list = ["1_white"] #, "2_white", "3_white", "4_white"]

    img_relative_path_list: list = []
    for folder in folder_list:
        file_list: list = CommonUtil.obtain_file_name_list(input_dir + folder + "/")[:1]
        for file in file_list:
            img_relative_path_list.append(folder + "/" + file)




    # Indicate which berry group is measured
    berry_group: str = "black"

    folder_list: list = ["1_" + berry_group, "2_" + berry_group, "3_" + berry_group, "4_" + berry_group]

    # Open/create csv file for berry group
    csv_file_name: str = 'measurement_'

    if berry_group == 'white':
        csv_file_name += 'white'
    else:
        csv_file_name += 'black'





    # Overwrite if csv already existed and add header
    with open(proj_file_output_dir_path + '/' + csv_file_name + '.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=",")

        # label, area, perimeter, convexity, concavity
        header = ['Label'] + ['Area'] + ['Perimeter'] + ['Convexity'] + ["Solidity"] + ["AverageHueManual"] + ["AverageHue"]
        writer.writerow(header)



    # Go through every ripeness group of the berry series
    for folder in folder_list:
        print('Image group ', folder, ' is now processed...')

        # Open csv file to append data
        with open(proj_file_output_dir_path + '/' + csv_file_name + '.csv', 'a', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=",")


            # To collect relative image paths of all images in folder
            img_relative_path_list: list = []


            # Output image directory
            output_dir_path: str = proj_output_dir_path + '/' + folder + '/'


            # ATM only first image of folder
            file_list: list = CommonUtil.obtain_file_name_list(input_dir + folder + "/")
            for file in file_list:
                img_relative_path_list.append(folder + "/" + file)

            # Go through every image
            for img_relative_path in img_relative_path_list:
                # TODO 46.Black_Mulberry_3 does not work
                # Obtain berry label/name
                img_name: str = img_relative_path.split("/")[-1].replace('.jpg', '')

                # Load current image, img[location][RGB channel]
                curr_img: diplib.ImageRead = ImageUtil.obtain_diplib_image(img_relative_path, input_dir)


                # ---------- Pre-processing ----------


                # Obtain size of image
                width, height = curr_img.Sizes()

                # Create new image to save single channel values
                new_img = diplib.Image((width, height), 1)

                # Subtract red channel (0) values from blue channel (2) values
                for i in range(len(curr_img)):
                    new_img[i] = curr_img[i][2] - curr_img[i][0]

                CommonUtil.save_image_to_folder(new_img, output_dir_path, img_name + '_processed.jpg')


                # ---------- Segmentation ----------

                # Segment image where object in pre-processed image is black and background white
                segm_img: diplib.Image = ImageUtil.segment_image_black(new_img)

                # Remove small objects
                segm_img = diplib.SmallObjectsRemove(segm_img, 1000)

                CommonUtil.save_image_to_folder(segm_img, output_dir_path, img_name + '_segmented.tif')


                # ---------- Measure features ----------

                # Obtain features in a list: area [0], perimeter [1], convexity [2], solidity (concavity?) [3]
                features: list = obtain_measurements(curr_img, segm_img)

                avg_hue_value: float = obtain_avg_hue(curr_img, segm_img)

                avg_hue_value_2: float = obtain_avg_hue_2(curr_img, segm_img)

                features.append(avg_hue_value)
                features.append(avg_hue_value_2)


                # ---------- Save in csv file ----------

                # Add the label of the image which is the ripeness of the berry
                label: str = folder.split("_")[0]
                features.insert(0, label)

                writer.writerow(features)




    # # print(img.ColorSpace())
    #
    # gray_scale_img = ImageUtil.convert_to_gray_scale(img);      ImageUtil.show_image_in_dip_view(gray_scale_img)
    # contrasted_img = diplib.ContrastStretch(gray_scale_img);    #ImageUtil.show_image_in_dip_view(contrasted_img)
    #
    # se_one_side_length = 50;    se_shape="elliptic"
    # o = ImageUtil.opening(contrasted_img, se_one_side_length, se_shape);        #ImageUtil.show_image_in_dip_view(o)
    #
    #
    # black_top_hat = ImageUtil.black_hat(contrasted_img, se_one_side_length, se_shape);      #ImageUtil.show_image_in_dip_view(black_top_hat)
    # # pix_list = ImageUtil.obtain_pixel_value_list(black_top_hat)
    # # p = PlotUtil.create_histogram_plot(pix_list)
    # # p.show()
    #
    # segment_img = ImageUtil.segment_image_white(black_top_hat);      ImageUtil.show_image_in_dip_view(segment_img)
    #
    # ws_img = diplib.Watershed(contrasted_img, segment_img, connectivity=2, flags={"binary", "high first"});      ImageUtil.show_image_in_dip_view(ws_img)
    # # ImageUtil.watershed(contrasted_img, segment_img)
    #
    #
    #
    #
    #
    #
    # segmentation_pixel_list = ImageUtil.obtain_pixel_value_list(segment_img)
    # img_rgb_tuple_list: list = ImageUtil.obtain_rgb_tuple_list(img)
    #
    # blue_pixel_list: list = ImageUtil.extract_blue_pixel_values(img_rgb_tuple_list);        ImageUtil.show_image_in_dip_view(img_rgb_tuple_list)
    #
    #
    # # print(segmentation_pixel_list)
    #
    # burries_rgb_tuple_list: list = []
    # for i in range(len(segmentation_pixel_list)):
    #     if segmentation_pixel_list[i] == True:
    #         burries_rgb_tuple_list.append(img_rgb_tuple_list[i])
    #
    #
    # # image = data.imread( input_dir + img_path)
    # pixel_list = ImageUtil.obtain_rgb_tuple_list_list(img)
    # avg_hue_value: float = ImageUtil.avg_hue_value(pixel_list)
    #
    # print("avg_hue_value", avg_hue_value)








    # histogram = ImageUtil.obtain_pixel_value_list(contrasted_img)
    # plot = PlotUtil.create_histogram_plot(histogram, plot_id=2, bins=256)
    # plot.show()
    #
    #
    # histogram = ImageUtil.obtain_pixel_value_list(gray_scale_img)
    # plot = PlotUtil.create_histogram_plot(histogram, plot_id=1, bins=256)
    # plot.show()


    CommonUtil.press_enter_to_exit()



    # ImageUtil.obtain_histogram_list

    CommonUtil.press_enter_to_continue()

    blackhat_img = ImageUtil.black_hat(gray_scale_img, se_one_side_length=60, se_shape="elliptic");    ImageUtil.show_image_in_dip_view(blackhat_img, title="blackhat_img")


    CommonUtil.press_enter_to_continue()




    # se_one_side_length: int = 10;   se_shape: str = "elliptic"
    # opening_img = ImageUtil.opening(gray_scale_img, se_one_side_length, se_shape);    ImageUtil.show_image_in_dip_view(opening_img)


    # eros_img = ImageUtil.threshold(gray_scale_img, se_one_side_length=10, se_shape="parabolic");          ImageUtil.show_image_in_dip_view(eros_img)
    threashold_img = ImageUtil.segment_image_white(blackhat_img);          ImageUtil.show_image_in_dip_view(threashold_img, title="threashold_img")

    watershed_img = ImageUtil.watershed(gray_scale_img, threashold_img);     ImageUtil.show_image_in_dip_view(watershed_img)

    CommonUtil.press_enter_to_exit()





    CommonUtil.press_enter_to_exit()