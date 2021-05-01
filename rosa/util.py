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
    def get_pattern(column_values: list):
        if len(column_values) > 0:
            while column_values[-1] == 0:
                column_values.pop()
            print(column_values)


    @staticmethod
    def calibrate(img: PyDIPjavaio.ImageRead):
        width, height = img.Sizes()

        print("Width: ", width)
        print("Height: ", height)

        column_candidates = []

        '''
        for i in range(width - 1):
            found_white_pixel = 0
            for j in range(height - 1):
                pixel_value = int(img.At(i, j)[0])
                if pixel_value == 1:
                    found_white_pixel = 1
            if found_white_pixel == 1:
                column_candidates.append(i)

        print(column_candidates)
        '''

        columns = []

        for i in range(width - 1):
            # found_first_white_pixel = 0
            column_pixels = []
            for j in range(height - 1):
                pixel_value = int(img.At(i, j)[0])

                if pixel_value == 1 and found_first_white_pixel == 0:
                    found_first_white_pixel = 1
                    column_pixels.append(pixel_value)

                if found_first_white_pixel == 1:
                    column_pixels.append(pixel_value)

            print("column ", i)
            UtilFunctions.get_pattern(column_pixels)
