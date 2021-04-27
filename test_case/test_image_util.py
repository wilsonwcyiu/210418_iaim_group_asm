from diplib import PyDIPjavaio

from util.common_util import CommonUtil
from util.image_util import ImageUtil


class TestImageUtil:



    @staticmethod
    def test_erosion():
        image_name_list: list = ["AxioCamIm01", "AxioCamIm02", "AxioCamIm03"]

        dir_path_str: int = CommonUtil.obtain_project_default_input_dir_path() + "asm3/"
        image_name: str = ""

        for image_name in image_name_list:
            original_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_image(image_name, dir_path=dir_path_str)
            threshold_img = ImageUtil.obtain_threshold_image(original_img)

            segment_size: int = 9
            erosion_img = ImageUtil.erosion(threshold_img, segment_size)

            ImageUtil.show_image_in_dip_view(erosion_img)