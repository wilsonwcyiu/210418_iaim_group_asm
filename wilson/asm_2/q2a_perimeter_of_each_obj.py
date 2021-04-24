from diplib import PyDIPjavaio

from util.common_util import CommonUtil
from util.image_util import ImageUtil


# test

if __name__ == '__main__':
    print("starting...")
    sleep_sec: int = 0

    image_name_list: list = ["rect1", "rect2", "rect3", "rect4"]


    date_time_str: str = CommonUtil.generate_date_time_str()
    for image_name in image_name_list:
        tmp_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_image(image_name)

        perimeter_list: list = ImageUtil.measure_perimeter_of_all_objects(tmp_img)

        print("image_name:", image_name, "\t",
              "perimeter_list:", perimeter_list
              )







