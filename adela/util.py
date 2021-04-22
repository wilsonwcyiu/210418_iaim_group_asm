import time
from datetime import datetime

import diplib
from diplib import PyDIPjavaio

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
        image_file_path = "../image_files/" + image_name
        print(image_file_path)

        img: PyDIPjavaio.ImageRead = diplib.ImageRead(image_file_path)

        return img


    @staticmethod
    def get_mean_std(values: []):
        mean = numpy.mean(values)
        std = numpy.std(values)

        return mean, std

    @staticmethod
    def print_largest_measurements(sizes: [], perimeters: []):
        index_sorted = numpy.flip((numpy.argsort(sizes)))

        sizes_top = []
        perimeters_top = []

        for i in index_sorted:
            if sizes[i] > 400:
                sizes_top.append(sizes[i])
                perimeters_top.append(perimeters[i])

        print("Only relevant objects:")
        print(sizes_top)
        print(perimeters_top)
        # size meadn and std
        s_mean, s_std = UtilFunctions.get_mean_std(sizes_top)
        print("sizes mean ", s_mean, " | sizes std ", s_std)

        # perimeter mean and std
        p_mean, p_std = UtilFunctions.get_mean_std(perimeters_top)
        print("perimeters mean ", p_mean, " | perimeters std ", p_std)
        print("----------------------------------")

        return s_mean, s_std, p_mean, p_std


    @staticmethod
    def threshold(img: PyDIPjavaio.ImageRead):
        _, threshold = diplib.Threshold(img)

        return threshold


    @staticmethod
    def show_image_in_dip_view(img: PyDIPjavaio.ImageRead, sleep_sec: int):
        diplib.PyDIPviewer.Show(img)
        time.sleep(sleep_sec)
