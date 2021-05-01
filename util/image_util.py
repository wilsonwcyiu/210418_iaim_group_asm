import sys
import time

import diplib
import numpy
from diplib import PyDIPjavaio
from diplib.PyDIP_bin import SE
from diplib.PyDIP_bin.MeasurementTool import MeasurementFeature, Measurement

from util.common_util import CommonUtil


class ImageUtil:

    # method ("linear","signed linear","logarithmic","signed logarithmic","erf","decade","sigmoid")
    # https://qiftp.tudelft.nl/dipref/ContrastStretch.html
    @staticmethod
    def increase_image_contrast(img: diplib.PyDIP_bin.Image):
        raise Exception("gives a correct display result but incorrect saved file (white blank file)")
        high_contrast_img: diplib.PyDIP_bin.Image = diplib.ContrastStretch(img, method="linear")

        return high_contrast_img



    @staticmethod
    def invert_img(img: diplib.PyDIP_bin.Image):

        return diplib.Invert(img)
        # return ~img


    @staticmethod
    def filter_image_by_threshold_value(img: diplib.PyDIP_bin.Image, threshold_value: float):
        filtered_img: diplib.PyDIP_bin.Image = img < threshold_value

        return filtered_img



    @staticmethod
    def subtraction_img1_minus_img2(img1: diplib.PyDIP_bin.Image, img2: diplib.PyDIP_bin.Image):
        raise Exception("problematic")
        subtracted_img: diplib.PyDIP_bin.Image = img1 > img2

        return subtracted_img



    @staticmethod
    def black_hat(img : diplib.PyDIP_bin.Image, se_one_side_length: int, se_shape: str):
        structuring_element: SE = diplib.PyDIP_bin.SE(shape=se_shape, param=se_one_side_length)
        black_hat_img: diplib.PyDIP_bin.Image = diplib.Tophat(img, structuring_element, polarity="black")

        # closing_img: diplib.PyDIP_bin.Image = ImageUtil.closing(img, se_one_side_length, se_shape)
        # black_hat_img: diplib.PyDIP_bin.Image = ImageUtil.subtraction_img1_minus_img2(closing_img, img)

        return black_hat_img



    @staticmethod
    def white_top_hat(img : diplib.PyDIP_bin.Image, se_one_side_length: int, se_shape: str):
        structuring_element: SE = diplib.PyDIP_bin.SE(shape=se_shape, param=se_one_side_length)
        # top_hat_img = diplib.Tophat(threshold_img, structuring_element)

        # works the same
        opening_img = ImageUtil.opening(img, se_one_side_length, se_shape)
        top_hat_img: diplib.PyDIP_bin.Image = ImageUtil.subtraction_img1_minus_img2(img, opening_img)

        return top_hat_img



    @staticmethod
    def opening(img : diplib.PyDIP_bin.Image, se_one_side_length: int, se_shape: str):
        structuring_element: SE = diplib.PyDIP_bin.SE(shape=se_shape, param=se_one_side_length)

        erosion_img: diplib.PyDIP_bin.Image = diplib.Erosion(img, se=structuring_element)
        opening_img: diplib.PyDIP_bin.Image = diplib.Dilation(erosion_img, se=structuring_element)

        return opening_img



    @staticmethod
    def closing(img : diplib.PyDIP_bin.Image, se_one_side_length: int, se_shape: str):
        structuring_element: SE = diplib.PyDIP_bin.SE(shape=se_shape, param=se_one_side_length)

        dilation_img: diplib.PyDIP_bin.Image = diplib.Dilation(img, se=structuring_element)
        closing_img: diplib.PyDIP_bin.Image = diplib.Erosion(dilation_img, se=structuring_element)

        return closing_img




    # https://github.com/DIPlib/diplib/blob/master/dipimage/erosion.m
    # % SYNOPSIS:
    # %  filterShape: 'rectangular', 'elliptic', 'diamond', 'parabolic'
    # %  image_se:    binary or grey-value image with the shape for the structuring element
    # %  boundary_condition: Defines how the boundary of the image is handled.
    # %                      See HELP BOUNDARY_CONDITION
    @staticmethod
    def dilation(img : diplib.PyDIP_bin.Image, se_one_side_length: int, se_shape: str):
        structuring_element: SE = diplib.PyDIP_bin.SE(shape=se_shape, param=se_one_side_length)
        dilation_img: diplib.PyDIP_bin.Image = diplib.Dilation(img, se=structuring_element)

        return dilation_img





    # https://github.com/DIPlib/diplib/blob/master/dipimage/erosion.m
    # % SYNOPSIS:
    # %  image_out = erosion(image_in,filterSize,filterShape,boundary_condition)
    # %  image_out = erosion(image_in,image_se,boundary_condition)
    # %
    # % PARAMETERS:
    # %  filterSize:  sizes of the filter along each image dimension
    # %  filterShape: 'rectangular', 'elliptic', 'diamond', 'parabolic'
    # %  image_se:    binary or grey-value image with the shape for the structuring element
    # %  boundary_condition: Defines how the boundary of the image is handled.
    # %                      See HELP BOUNDARY_CONDITION
    @staticmethod
    def erosion(img : diplib.PyDIP_bin.Image, se_one_side_length: int, se_shape: str):

        structuring_element: SE = diplib.PyDIP_bin.SE(shape=se_shape, param=se_one_side_length)
        erosion_img: diplib.PyDIP_bin.Image = diplib.Erosion(img, se=structuring_element)

        return erosion_img





    @staticmethod
    def calculate_signal_to_noise_ratio_SNR(original_img: diplib.PyDIP_bin.Image):
        pixel_value_list: list = ImageUtil.obtain_pixel_value_list(original_img)

        mean: float = numpy.mean(pixel_value_list)
        standard_dev: float = numpy.std(pixel_value_list)

        snr: float = mean / standard_dev

        return snr



    @staticmethod
    def sum_of_pixel_value(img: PyDIPjavaio.ImageRead):
        pixel_value_list: list = ImageUtil.obtain_pixel_value_list(img)

        sum_of_pixel_value: float = numpy.sum(pixel_value_list)

        return sum_of_pixel_value



    @staticmethod
    def obtain_histogram_list(img: PyDIPjavaio.ImageRead):
        pixel_value_list: list = ImageUtil.obtain_pixel_value_list(img)

        max_pixel_value: int = max(pixel_value_list)

        if max_pixel_value < 256:
            max_value = 256


        histogram_list: list = [0] * max_value


        for pixel_location in range(len(img)):
            pixel_value = img[pixel_location][0]
            histogram_list[pixel_value] += 1

        return histogram_list




    @staticmethod
    def calc_snr(img: PyDIPjavaio.ImageRead):
        pixel_value_list: list = ImageUtil.obtain_pixel_value_list(img)

        mean: float = CommonUtil.calc_mean(pixel_value_list)
        standard_deviation: float = CommonUtil.calc_standard_deviation(pixel_value_list, mean)

        snr: float = mean / standard_deviation

        return snr



    @staticmethod
    def obtain_pixel_value_list(img: PyDIPjavaio.ImageRead):
        pixel_value_list: list = []

        for pixel_location in range(len(img)):
            pixel_value: int = int(img[pixel_location][0])
            pixel_value_list.append(pixel_value)

        return pixel_value_list




    @staticmethod
    def detect_number_of_objects(threshold_img: diplib.PyDIP_bin.Image, original_img: diplib.PyDIP_bin.Image):
        labeled_img = diplib.Label(threshold_img)

        measurements = diplib.MeasurementTool.Measure(labeled_img, original_img, ['Size'])

        number_of_objects: int = 0
        for object in numpy.array(measurements):
            number_of_objects += 1

        return number_of_objects




    @staticmethod
    def obtain_convexity(threshold_img: diplib.PyDIP_bin.Image, original_img: diplib.PyDIP_bin.Image):
        labeled_img = diplib.Label(threshold_img)

        measurements = diplib.MeasurementTool.Measure(labeled_img, original_img, ['Convexity'])

        convenity_list: list = []
        for object in numpy.array(measurements):
            convenity_list.append(object[0])

        return convenity_list



    @staticmethod
    def obtain_solidity(threshold_img: diplib.PyDIP_bin.Image, original_img: diplib.PyDIP_bin.Image):
        labeled_img = diplib.Label(threshold_img)

        measurements = diplib.MeasurementTool.Measure(labeled_img, original_img, ['Solidity'])

        solidity_list: list = []
        for object in numpy.array(measurements):
            solidity_list.append(object[0])

        return solidity_list


    @staticmethod
    def obtain_threshold_image_by_given_value(img: diplib.PyDIP_bin.Image, threshold_value: float):
        threshold_img: diplib.PyDIP_bin.Image = img < threshold_value

        return threshold_img


    @staticmethod
    def obtain_threshold_image(img: diplib.PyDIP_bin.Image):
        threshold_value: float = ImageUtil.derive_threshold_value(img);     #print("134234 threshold_value", threshold_value)
        threshold_img: diplib.PyDIP_bin.Image = img < threshold_value

        return threshold_img



    @staticmethod   # median_kernel_para_list = ['rectangular', 'elliptic']
    def median_filter(img, median_kernel_side_length: str):
        filtered_img = diplib.MedianFilter(img, median_kernel_side_length)

        return filtered_img



    # @staticmethod
    # def measure_perimeter_of_all_objects(img: PyDIPjavaio.ImageRead):
    #     threshold_value = ImageUtil.threshold(img)
    #
    #     # Segment image
    #     segm_img = img < threshold_value
    #
    #     # Label segmented objects
    #     segm_img = diplib.Label(segm_img)
    #
    #     px_measurements = diplib.MeasurementTool.Measure(segm_img, img, ['Perimeter'])
    #
    #     tmp: MeasurementFeature = px_measurements['Perimeter']
    #
    #     numpy_list = numpy.array(tmp).transpose()[0]
    #     perimeter_list: list = numpy_list.tolist()
    #
    #     return perimeter_list



    @staticmethod
    def measure_perimeter_of_all_objects(threshold_image, img: PyDIPjavaio.ImageRead):
        labeled_img = diplib.Label(threshold_image)

        px_measurements = diplib.MeasurementTool.Measure(labeled_img, img, ['Perimeter'])

        tmp: MeasurementFeature = px_measurements['Perimeter']

        numpy_list = numpy.array(tmp).transpose()[0]
        perimeter_list: list = numpy_list.tolist()

        return perimeter_list



    # @staticmethod
    # def measure_surface_area_of_all_objects(img: PyDIPjavaio.ImageRead):
    #     threshold_value: float = ImageUtil.threshold(img)
    #
    #     # Segment image
    #     segm_img: diplib.PyDIP_bin.Image = img < threshold_value
    #
    #     # Label segmented objects
    #     segm_img: diplib.PyDIP_bin.Image = diplib.Label(segm_img)
    #
    #     px_measurements: Measurement = diplib.MeasurementTool.Measure(segm_img, img, ['Size'])
    #
    #     tmp: MeasurementFeature = px_measurements['Size']
    #
    #     numpy_list = numpy.array(tmp).transpose()[0]
    #     surface_area_list: list = numpy_list.tolist()
    #
    #     return surface_area_list


    @staticmethod
    def measure_surface_area_of_all_objects(threshold_image, img: PyDIPjavaio.ImageRead):
        labeled_img = diplib.Label(threshold_image)

        px_measurements: Measurement = diplib.MeasurementTool.Measure(labeled_img, img, ['Size'])

        tmp: MeasurementFeature = px_measurements['Size']

        numpy_list = numpy.array(tmp).transpose()[0]
        surface_area_list: list = numpy_list.tolist()

        return surface_area_list




    @staticmethod
    def median_filter(img: PyDIPjavaio.ImageRead, median_parameter: int):
        filtered_img = diplib.MedianFilter(img, median_parameter)
        return filtered_img



    @staticmethod
    def gauss_filter(img: PyDIPjavaio.ImageRead, sigmas: int):
        gauss_img: diplib.PyDIP_bin.Image = diplib.Gauss(img, sigmas)
        # threshold_value: float = ImageUtil.threshold(gauss_img)
        # filtered_img: diplib.PyDIP_bin.Image = gauss_img < threshold_value

        return gauss_img



    @staticmethod
    def derive_threshold_value(img: PyDIPjavaio.ImageRead):
        threshold_value: float = None
        _, threshold_value = diplib.Threshold(img)

        return threshold_value



    @staticmethod
    def show_image_in_dip_view(img: PyDIPjavaio.ImageRead, sleep_sec: int = 0, title="No title", position_tuple=None):
        if position_tuple is not None:
            diplib.PyDIPviewer.Show(img, title=title, position=position_tuple)
        else:
            diplib.PyDIPviewer.Show(img, title=title)

        time.sleep(sleep_sec)




    @staticmethod
    def obtain_image(image_name: str, dir_path: str = None):
        if dir_path is None:
            dir_path = CommonUtil.obtain_project_default_input_dir_path()

        image_file_path = dir_path + image_name
        # image_file_path = "../../image_files/" + image_name

        try:
            img: PyDIPjavaio.ImageRead = diplib.ImageRead(image_file_path)
        except Exception as e:
            print("image_file_path", image_file_path)
            raise e

        return img



    @staticmethod
    def measure_size_and_perimeter(image: PyDIPjavaio.ImageRead, iso_threshold: int):
        # iso_threshold: int = 65
        rectangles = image < iso_threshold
        rectangles = diplib.Label(rectangles)

        px_measure: diplib.PyDIP_bin.MeasurementTool.Measurement = diplib.MeasurementTool.Measure(rectangles, image, ['Size', 'Perimeter'])

        # print("px_measure: ", type(px_measure), px_measure)

        size_list = numpy.array(px_measure['Size']).transpose()
        perimeter_list = numpy.array(px_measure['Perimeter']).transpose()

        return size_list, perimeter_list


    @staticmethod
    def threshold(image: PyDIPjavaio.ImageRead):
        _, threshold = diplib.Threshold(image, method='otsu')

        return threshold


    @staticmethod
    def segment_image_white(image: PyDIPjavaio.ImageRead):
        # function for segmentation of white shapes on black background
        threshold = ImageUtil.threshold(image)

        return image > threshold


    @staticmethod
    def segment_image_black(image: PyDIPjavaio.ImageRead):
        # function for segmentation of black shapes on white background
        threshold = ImageUtil.threshold(image)

        return image < threshold
