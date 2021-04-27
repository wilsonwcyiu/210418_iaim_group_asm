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
        original_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_image(image_name)
        threshold_img = ImageUtil.obtain_threshold_image(original_img)

        surface_area_list: list = ImageUtil.measure_surface_area_of_all_objects(threshold_img, original_img)


        print("image_name:", image_name, "\t",
              "surface_area_list:", surface_area_list
              )







