import time
from datetime import datetime

import diplib
from diplib import PyDIPjavaio

import matplotlib.pyplot as plt

import numpy

class UtilFunctions:


    @staticmethod
    def generate_date_time_str():
        date_time_str = str(datetime.now().strftime("%Y-%m-%d_%H%M%S"))
        return date_time_str


    @staticmethod
    def save_image_to_default_project_folder(img: PyDIPjavaio.ImageRead, image_name: str):
        PyDIPjavaio.ImageWrite(img, "../../image_output/" + image_name)


    @staticmethod
    def sleep(secs: int):
        time.sleep(secs)


    @staticmethod
    def obtain_image(image_name: str):
        image_file_path = "../image_files/asm3/" + image_name
        print(image_file_path)

        img: PyDIPjavaio.ImageRead = diplib.ImageRead(image_file_path)

        return img


    @staticmethod
    def get_mean_std(values: list):
        mean = numpy.mean(values)
        std = numpy.std(values)

        return mean, std


    @staticmethod
    def threshold(img: PyDIPjavaio.ImageRead):
        _, threshold = diplib.Threshold(img, method='otsu')

        return threshold


    @staticmethod
    def segment_image(img: PyDIPjavaio.ImageRead):
        threshold_value = UtilFunctions.threshold(img)
        segm_img = img > threshold_value
        return segm_img


    @staticmethod
    def show_image_in_dip_view(img: PyDIPjavaio.ImageRead, sleep_sec: int):
        diplib.PyDIPviewer.Show(img)
        #diplib.Show(img)
        time.sleep(sleep_sec)


    @staticmethod
    def get_pixel_values(img: PyDIPjavaio.ImageRead):
        pixel_value_list = []

        for pixel_location in range(len(img)):
            list_entry = img[pixel_location]
            pixel_value_list = numpy.append(pixel_value_list, int(list_entry[0]))

        return pixel_value_list


    @staticmethod
    def get_intensity_range(pixel_values: list):
        return max(pixel_values), min(pixel_values)

    @staticmethod
    def get_histogram(pixel_values: list, image_name: str):
        #max_value, min_value = UtilFunctions.get_intensity_range(pixel_values)
        bin_list = list(range(0, 255))
        plt.hist(pixel_values, bins=bin_list)
        plt.title('Histogram of ' + image_name)
        plt.xlabel('Intensity values')
        plt.ylabel('Frequency')
        plt.show()


    @staticmethod
    def get_numerical_statistics(pixel_values: list, image_name: str):
        max_value, min_value = UtilFunctions.get_intensity_range(pixel_values)
        mean_value = numpy.mean(pixel_values)

        print("Minimum intensity value of ", image_name, ": ", min_value)
        print("Maximum intensity value of ", image_name, ": ", max_value)

        print("Average intensity value of ", image_name, ": ", mean_value)


    @staticmethod
    def black_hat_transf(img: PyDIPjavaio.ImageRead):
        struct_elem = diplib.PyDIP_bin.SE(shape='elliptic', param=71)
        return diplib.Tophat(img, struct_elem, polarity="black")


    @staticmethod
    def gaussian_filter(img: PyDIPjavaio.ImageRead, sigma: int):
        return diplib.Gauss(img, sigma)


    @staticmethod
    def remove_irrelevant_parts(column_values: list):
        while column_values[0] == 0 and len(column_values) > 1:
            column_values.pop(0)

        while column_values[-1] == 0 and len(column_values) > 1:
            column_values.pop()

        return column_values


    @staticmethod
    def get_pattern_of_column(column_values: list):
        pattern = []
        # Already count the first pixel value
        count = 1
        for i in range(1, len(column_values)-1):
            if column_values[i] == column_values[i-1]:
                count += 1
            else:
                pattern.append(count)
                count = 1
        return pattern


    @staticmethod
    def calibrate(img: PyDIPjavaio.ImageRead):
        width, height = img.Sizes()

        print("Width: ", width)
        print("Height: ", height)

        # Odd are black pixels
        column_patterns = []

        for i in range(width - 1):
            column_pixels = []
            for j in range(height - 1):
                pixel_value = int(img.At(i, j)[0])
                column_pixels.append(pixel_value)

            new_column_pixels = UtilFunctions.remove_irrelevant_parts(column_pixels)

            if len(new_column_pixels) > 1:
                # Get pattern
                column_pattern = UtilFunctions.get_pattern_of_column(new_column_pixels)
                column_patterns.append(column_pattern)

        column_patterns.sort(key=len)
        print("Column with highest transition rate:")
        print(column_patterns[-1])
