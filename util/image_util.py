import time

import diplib
import numpy
from diplib import PyDIPjavaio
from diplib.PyDIP_bin.MeasurementTool import MeasurementFeature, Measurement

from util.common_util import CommonUtil


class ImageUtil:

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


        histogram_list: list = ([0] * max_value) + 1


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
    def obtain_threshold_image(img: diplib.PyDIP_bin.Image):
        threshold_value: float = ImageUtil.threshold(img)
        threshold_img: diplib.PyDIP_bin.Image = img < threshold_value

        return threshold_img



    @staticmethod   # median_kernel_para_list = ['rectangular', 'elliptic']
    def median_filter(img, median_kernel_para: str):
        filtered_img = diplib.MedianFilter(img, median_kernel_para)

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
    def threshold(img: PyDIPjavaio.ImageRead):
        threshold: float = None
        _, threshold = diplib.Threshold(img)

        return threshold



    @staticmethod
    def show_image_in_dip_view(img: PyDIPjavaio.ImageRead, sleep_sec: int = 0, title="No title"):
        diplib.PyDIPviewer.Show(img, title=title)
        time.sleep(sleep_sec)




    @staticmethod
    def obtain_image(image_name: str):
        dir_path = CommonUtil.obtain_project_default_output_file_path("image_files")
        image_file_path = dir_path + image_name
        # image_file_path = "../../image_files/" + image_name

        img: PyDIPjavaio.ImageRead = diplib.ImageRead(image_file_path)

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
