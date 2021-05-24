import sys
import time

import diplib
import imageio
import numpy
from diplib import PyDIPjavaio
from diplib.PyDIP_bin import SE
from diplib.PyDIP_bin.MeasurementTool import MeasurementFeature, Measurement
from matplotlib import pyplot
from skimage import color

from util.common_util import CommonUtil

from skimage.io import imread

class ImageUtil:



    @staticmethod
    def extract_blue_pixel_values(rgb_tuple_list: numpy.ndarray):
        blue_pixel_list: list = []
        for rgb_tuple in rgb_tuple_list:
            blue_pixel_list.append(rgb_tuple[2])

        return blue_pixel_list



    # https://www.programmersought.com/article/54406295171/
    # Takes an image file name, calculates the average hue value of the whole image and returns the value
    # image needs to be in the directory the notebook is running in.
    @staticmethod
    def avg_hue_value(rgb_tuple_list: numpy.ndarray):
        if isinstance(rgb_tuple_list, list):
            rgb_tuple_list = CommonUtil.list_to_ndarray(rgb_tuple_list)


        img_hsv: numpy.ndarray = color.rgb2hsv(rgb_tuple_list)

        sum: float = 0

        for i in range(0, len(img_hsv)):
            for j in range(0, len(img_hsv[0])):
                sum = sum + img_hsv[i][j]#[0]

        avg_hue_value: float = sum / (len(img_hsv)*len(img_hsv[0]))


        return avg_hue_value





    @staticmethod
    def obtain_rgb_tuple_list(img: PyDIPjavaio.ImageRead):
        pixel_value_tuple_list: list = []

        for pixel_location in range(len(img)):
            rgb_tuple: tuple = (img[pixel_location][0], img[pixel_location][1], img[pixel_location][2])
            pixel_value_tuple_list.append(rgb_tuple)

        return pixel_value_tuple_list



    @staticmethod
    def obtain_rgb_tuple_list_list(img: PyDIPjavaio.ImageRead):
        pixel_value_tuple_list: list = []

        for pixel_location in range(len(img)):
            rgb_tuple: tuple = [img[pixel_location][0], img[pixel_location][1], img[pixel_location][2]]
            pixel_value_tuple_list.append(rgb_tuple)

        return pixel_value_tuple_list




    @staticmethod
    def watershed(img: diplib.PyDIP_bin.Image, mask_img: diplib.PyDIP_bin.Image):
        watershed_img: diplib.Image = diplib.Watershed(img, mask_img, connectivity=2, flags={"binary", "high first"})

        return watershed_img


    #https://notebook.community/DIPlib/diplib/examples/python/pydip_basics
    @staticmethod
    def diplib_convert(diplib_img: diplib.PyDIP_bin.Image, convert_str: str):
        if convert_str not in ['Lab', 'gray', 'sRGB', 'RGB']:
            raise Exception()

        convert_img: diplib.PyDIP_bin.Image = diplib.ColorSpaceManager.Convert(diplib_img, convert_str)

        return convert_img



    @staticmethod
    def convert_to_gray_scale(diplib_img: diplib.PyDIP_bin.Image):
        gray_scale_img: diplib.PyDIP_bin.Image = diplib.ColorSpaceManager.Convert(diplib_img, 'gray')

        return gray_scale_img



    @staticmethod
    def obtain_image_gray_array(image_path: str):
        image_gray_array: numpy.ndarray = imread(image_path, as_gray=True)

        return image_gray_array




    @staticmethod
    def obtain_image_rgb_array(image_path: str):
        img_rgb_array: numpy.ndarray = imread(image_path)

        return img_rgb_array




    @staticmethod
    def create_multi_img_plot(img_rgb_array_list: list, total_rows: int, total_col: int, window_size_tuple: tuple):
        img_idx = 1

        fig = pyplot.figure(figsize=window_size_tuple)
        for img_rgb_array in img_rgb_array_list:
            fig.add_subplot(total_rows, total_col, img_idx)
            pyplot.imshow(img_rgb_array)

            img_idx += 1

        return pyplot



    @staticmethod
    def obtain_image_width_height(dip_image: diplib.Image):
        width: int = dip_image.Sizes()[0]
        height: int = dip_image.Sizes()[1]

        return width, height



    @staticmethod
    def obtain_column_pixel_value_list(img: diplib.PyDIP_bin.Image):
        size_list: list = img.Sizes();
        total_col: int = size_list[0]
        total_row: int = size_list[1]

        pixel_value_list: list = []
        for col_idx in range (0, total_col):
            col_list: list = []
            for row_idx in range (0, total_row):
                pixel = img.At(col_idx, row_idx)
                pixel_value: int = int(pixel[0])
                col_list.append(pixel_value)

            pixel_value_list.append(col_list)

        return pixel_value_list




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
        top_hat_img = diplib.Tophat(img, structuring_element, polarity="white")

        # works the same
        # opening_img = ImageUtil.opening(img, se_one_side_length, se_shape)
        # top_hat_img: diplib.PyDIP_bin.Image = ImageUtil.subtraction_img1_minus_img2(img, opening_img)

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
            pixel_value = img[pixel_location][0]
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
    def median_filter(img, median_kernel_side_length: int):
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
        _, threshold_value = diplib.Threshold(img, method = 'otsu')

        return threshold_value



    # img: PyDIPjavaio.ImageRead; img: ndarray
    @staticmethod
    def show_image_in_dip_view(img: PyDIPjavaio.ImageRead, sleep_sec: int = 0, title="No title", position_tuple=None):
        if position_tuple is not None:
            diplib.PyDIPviewer.Show(img, title=title, position=position_tuple)
        else:
            diplib.PyDIPviewer.Show(img, title=title)

        time.sleep(sleep_sec)




    @staticmethod
    def obtain_diplib_image(image_name: str, dir_path: str = None):
        if dir_path is None:
            dir_path = CommonUtil.obtain_project_default_input_dir_path()

        image_file_path = dir_path + image_name

        diplib_img: PyDIPjavaio.ImageRead = None
        try:
            img_extension: str = CommonUtil.obtain_file_extension(image_name)
            if img_extension.lower() in ("jpeg", "jpg"):     diplib_img = diplib.ImageReadJPEG(image_file_path)
            elif img_extension.lower() in ("png"):           diplib_img = diplib.ImageRead(image_file_path)
            elif img_extension.lower() in ("tif", "tiff"):   diplib_img = diplib.ImageReadTIFF(image_file_path)
            else: diplib_img = diplib.ImageRead(image_file_path)


        except Exception as e:
            print("image_file_path", image_file_path)
            raise e

        return diplib_img


    @staticmethod
    def obtain_image_imageio(image_name: str, dir_path: str = None):
        if dir_path is None:
            dir_path = CommonUtil.obtain_project_default_input_dir_path()

        image_file_path = dir_path + image_name
        # image_file_path = "../../image_files/" + image_name

        try:
            img = imageio.imread(image_file_path)
            image = diplib.PyDIP_bin.Image(img)
        except Exception as e:
            print("image_file_path", image_file_path)
            raise e

        return image



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
