import math
import os
import time
from datetime import datetime

from diplib import PyDIPjavaio
from os import path

import json
import os
from datetime import datetime
from decimal import Decimal

import matplotlib.pyplot as plt
import numpy as np

class CommonUtil:

    @staticmethod
    def derive_relative_error(float_list: list):
        mean: float = CommonUtil.calc_mean(float_list)
        std_dev: float = CommonUtil.calc_standard_deviation(float_list, mean)

        square_root_of_perimeter_mean: float = CommonUtil.square_root(mean)
        coefficient_of_variation: float = std_dev / mean

        return square_root_of_perimeter_mean, coefficient_of_variation



    @staticmethod
    def press_enter_to_continue():
        input("Press enter to end the process...")



    @staticmethod
    def square_root(data: float):
        square_root: float = math.sqrt(data)
        return square_root



    @staticmethod
    def numpy_array_to_python_list(numpy_array):
        python_list: list = numpy_array.to_list()
        return python_list



    @staticmethod
    def generate_date_time_str():
        date_time_str = str(datetime.now().strftime("%Y-%m-%d_%H%M%S"))
        return date_time_str


    # @staticmethod
    # def save_image_to_default_project_folder(img: PyDIPjavaio.ImageRead, file_name: str):
    #     CommonUtil.save_image_to_default_project_folder(img=img, dir_name=None, file_name=file_name)


    @staticmethod
    def save_image_to_default_project_folder(img: PyDIPjavaio.ImageRead, dir_name: str, file_name: str):
        project_dir: str = "../../image_output/"
        dir_path_str: str = os.path.join(project_dir, dir_name)
        full_file_path: str = os.path.join(dir_path_str, file_name)

        if dir_name is not None and not path.exists(dir_path_str):
            os.mkdir(dir_path_str, 0x0755)
            print("dir_path_str", dir_path_str)

        PyDIPjavaio.ImageWrite(img, full_file_path)



    @staticmethod
    def sleep(secs: int):
        time.sleep(secs)



    @staticmethod
    def print_on_same_line(text: str):
        print("\r", text, end='')



    @staticmethod
    def generate_date_time_str():
        date_time_str = str(datetime.now().strftime("%Y-%m-%d_%H%M%S"))
        return date_time_str


    @staticmethod
    def make_dir(abs_dir_path):
        os.mkdir(abs_dir_path)



    @staticmethod
    def write_txt_file(data_list, abs_file_path):
        f = open(abs_file_path, "a")
        for data in data_list:
            f.write(str(data) + "\n")

        f.close()



    @staticmethod
    def read_txt_file(abs_file_path):
        #open and read the file after the appending:
        f = open(abs_file_path, "r")
        print(f.read())

        raise Exception("TBC")



    # 1, 1000 -> 0001
    @staticmethod
    def format_int_to_str_length(number: int, to_length: int):
        return str(number).zfill(to_length)



    @staticmethod
    def save_json_to_file(data_dict: dict, abs_file_path_str: str):
        file1 = open(abs_file_path_str, "w")
        file1.writelines(json.dumps(data_dict, indent=4))





    @staticmethod
    def round_tuple_values_to_hundredths(float_tuple):
        result_tuple = tuple([Decimal(el).quantize(Decimal(".01")) for el in float_tuple])
        return result_tuple


    @staticmethod
    def round_to_hundredths(float_data):
        rounded_float = Decimal(float_data).quantize(Decimal(".01"))
        return rounded_float


    @staticmethod
    def calc_mean(data_list):
        mean: float = sum(data_list)/len(data_list)

        return mean


    @staticmethod
    def calc_standard_deviation(data_list, mean):
        variance: float = sum([((data - mean) ** 2) for data in data_list]) / len(data_list)
        stddev: float = variance ** 0.5

        return stddev



