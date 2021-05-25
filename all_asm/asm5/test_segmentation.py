# Segmentation of berry images

import diplib
import numpy as np
from diplib.PyDIP_bin.MeasurementTool import MeasurementFeature, Measurement

from util.common_util import CommonUtil
from util.image_util import ImageUtil

import numpy

import csv


# Only obtain the measurements of the object that represents the berry
def obtain_largest_object_measurements(measurements_all_objects: Measurement):
    # Collect measurements
    sizes: numpy.array = numpy.array(measurements_all_objects['Size']).transpose()
    perimeters: numpy.array = numpy.array(measurements_all_objects['Perimeter']).transpose()
    convexities: numpy.array = numpy.array(measurements_all_objects['Convexity']).transpose()
    solidities: numpy.array = numpy.array(measurements_all_objects['Solidity']).transpose()

    # Get index of largest object (berry) in measurement lists
    index_largest_object: int = numpy.argmax(sizes)

    # Get feature list of berry
    features_largest_object: list = [sizes[0][index_largest_object], perimeters[0][index_largest_object],
                                     convexities[0][index_largest_object], solidities[0][index_largest_object]]

    return features_largest_object


# Obtain shape/hue features in list area [0], perimeter [1], convexity [2], solidity (concavity?) [3]
def obtain_measurements(rgb_img: diplib.Image, segmented_img: diplib.Image):

    labeled_img: diplib.Image = diplib.Label(segmented_img)

    measurements: Measurement = diplib.MeasurementTool.Measure(labeled_img, rgb_img, ['Size', 'Perimeter', 'Convexity', 'Solidity'])

    # Get features of only the largest object (berry) if there are still irrelevant objects present
    feature_list = obtain_largest_object_measurements(measurements)

    return feature_list


if __name__ == '__main__':

    # Configure files and directories
    input_dir: str = CommonUtil.obtain_project_default_input_dir_path() + 'asm5/'
    proj_file_output_dir_path: str = '../../file_output/asm5'
    proj_output_dir_path: str = '../../image_output/asm5'
    img_extension: str = ""

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
        header = ['Label'] + ['Area'] + ['Perimeter'] + ['Convexity'] + ["Solidity"]
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


                # ---------- Save in csv file ----------

                # Add the label of the image which is the ripeness of the berry
                label: str = folder.split("_")[0]
                features.insert(0, label)

                writer.writerow(features)




