import json
import math
import os
import pprint
import time
from datetime import datetime
from decimal import Decimal
from os import path
from turtle import pd

import pandas
from diplib import PyDIPjavaio


class CommonUtil:


    @staticmethod
    def press_enter_to_exit():
        input("Press enter to exit...")
        exit(0)


    @staticmethod
    def create_missing_dir(dir_path_str: str):
        if not path.exists(dir_path_str):
            os.mkdir(dir_path_str, 0x0755)



    @staticmethod
    def print_complete_panda_data_frame(data_frame):
        with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
            print(data_frame)



    @staticmethod
    def obtain_project_default_input_dir_path(project_file_output_dir_name: str = "image_files", max_layers: int = 20):
        parent_dir: str = os.getcwd()

        project_default_input_dir_path: str = ""
        layer_idx: int = 0
        while True:
            for root, sub_dir_name_list, files in os.walk(parent_dir):
                for sub_dir_name in sub_dir_name_list:
                    if sub_dir_name == project_file_output_dir_name:
                        project_default_input_dir_path += project_file_output_dir_name + "/"
                        return project_default_input_dir_path


            parent_dir, dir_name = os.path.split(parent_dir)
            if dir_name != project_file_output_dir_name:
                project_default_input_dir_path += "../"

            elif dir_name == project_file_output_dir_name:
                project_default_input_dir_path += dir_name + "/"
                return project_default_input_dir_path


            layer_idx += 1
            if layer_idx == max_layers:
                err_msg: str = "directory " + project_file_output_dir_name + " not exist in the " + str(max_layers) + " layer above"
                raise Exception(err_msg)



    @staticmethod
    def filter_list_value_smaller_than(data_list: int, filter_value: int):
        filtered_list: list = []
        for data in data_list:
            if data > filter_value:
                filtered_list.append(data)

        return filtered_list



    @staticmethod
    def obtain_project_default_output_dir_path(project_file_output_dir_name: str = "file_output", max_layers: int = 20):
        parent_dir: str = os.getcwd()

        project_default_output_file_path: str = ""
        layer_idx: int = 0
        while True:
            for root, sub_dir_name_list, files in os.walk(parent_dir):
                for sub_dir_name in sub_dir_name_list:
                    if sub_dir_name == project_file_output_dir_name:
                        project_default_output_file_path += project_file_output_dir_name + "/"
                        return project_default_output_file_path


            parent_dir, dir_name = os.path.split(parent_dir)
            if dir_name != project_file_output_dir_name:
                project_default_output_file_path += "../"

            elif dir_name == project_file_output_dir_name:
                project_default_output_file_path += dir_name + "/"
                return project_default_output_file_path


            layer_idx += 1
            if layer_idx == max_layers:
                err_msg: str = "directory " + project_file_output_dir_name + " not exist in the " + str(max_layers) + " layer above"
                raise Exception(err_msg)




    # players = [{'dailyWinners': 3, 'dailyFreePlayed': 2, 'user': 'Player1', 'bank': 0.06},
    #            {'dailyWinners': 3, 'dailyFreePlayed': 2, 'user': 'Player2', 'bank': 4.0},
    #            {'dailyWinners': 1, 'dailyFree': 2, 'user': 'Player3', 'bank': 3.1}]
    @staticmethod
    def write_list_of_dict_to_excel(list_of_dict: dict, file_path: str):
        parent_dir, dir_name = os.path.split(file_path)

        if dir_name is not None and not path.exists(parent_dir):
            os.mkdir(parent_dir, 0x0755)

        df = pandas.DataFrame.from_dict(list_of_dict)
        df.to_excel(file_path)



    @staticmethod
    def calc_coefficient_of_variation_CV(mean: float, standard_deviation: float):
        cv: float = mean / standard_deviation

        return cv



    @staticmethod
    def pretty_print(obj: object, width=100):
        pprint.pprint(obj, width=width)



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



    @staticmethod
    def save_image_to_folder(img: PyDIPjavaio.ImageRead, dir_path_str: str, file_name: str):
        if not path.exists(dir_path_str):
            os.mkdir(dir_path_str, 0x0755)

        full_file_path: str = os.path.join(dir_path_str, file_name)

        PyDIPjavaio.ImageWrite(img, full_file_path)



    @staticmethod
    def save_image_to_default_project_folder(img: PyDIPjavaio.ImageRead, dir_name: str, file_name: str):
        project_dir: str = "../../image_output/"
        dir_path_str: str = os.path.join(project_dir, dir_name)
        full_file_path: str = os.path.join(dir_path_str, file_name)

        if dir_name is not None and not path.exists(dir_path_str):
            os.mkdir(dir_path_str, 0x0755)

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



