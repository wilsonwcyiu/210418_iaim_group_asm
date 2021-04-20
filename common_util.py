
import time
from datetime import datetime

from diplib import PyDIPjavaio


class CommonUtil:


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