from diplib import PyDIPjavaio

from util.common_util import CommonUtil
from util.image_util import ImageUtil


# test_case

if __name__ == '__main__':
    print("starting...")
    sleep_sec: int = 0

    image_name_list: list = ["rect1", "rect2", "rect3", "rect4"]


    date_time_str: str = CommonUtil.generate_date_time_str()
    for image_name in image_name_list:
        original_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_diplib_image(image_name)
        threshold_img = ImageUtil.obtain_threshold_image(original_img)

        perimeter_list: list = ImageUtil.measure_perimeter_of_all_objects(threshold_img, original_img)
        mean: float = CommonUtil.calc_mean(perimeter_list)
        std_dev: float = CommonUtil.calc_standard_deviation(perimeter_list, mean)

        print("image_name:", image_name, "\t",
              "mean:", mean, "\t",
              "std_dev:", std_dev
              )




