import time

import diplib
import numpy
from diplib import PyDIPjavaio
from diplib.PyDIP_bin.MeasurementTool import MeasurementFeature, Measurement


class ImageUtil:

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
        threshold_value: float = ImageUtil.threshold(gauss_img)
        filtered_img: diplib.PyDIP_bin.Image = gauss_img < threshold_value

        return gauss_img



    @staticmethod
    def threshold(img: PyDIPjavaio.ImageRead):
        threshold: float = None
        _, threshold = diplib.Threshold(img)

        return threshold



    @staticmethod
    def show_image_in_dip_view(img: PyDIPjavaio.ImageRead, sleep_sec: int = 0):
        diplib.PyDIPviewer.Show(img)
        time.sleep(sleep_sec)




    @staticmethod
    def obtain_image(image_name: str):
        image_file_path = "../../image_files/" + image_name

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
