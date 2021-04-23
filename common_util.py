import os
import time
from datetime import datetime

from diplib import PyDIPjavaio
from os import path


class CommonUtil:


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