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

        surface_area_list: list = ImageUtil.measure_surface_area_of_all_objects(tmp_img)
        mean: float = CommonUtil.calc_mean(surface_area_list)
        std_dev: float = CommonUtil.calc_standard_deviation(surface_area_list, mean)

        print("image_name", image_name, "\t",
              "mean", mean, "\t",
              "std_dev", std_dev
              )




