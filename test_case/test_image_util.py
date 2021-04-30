from diplib import PyDIPjavaio

from util.common_util import CommonUtil
from util.image_util import ImageUtil


class TestImageUtil:

    @staticmethod
    def top_hat_test1():
        image_name_list: list = ["AxioCamIm01"]
            # , "AxioCamIm02", "AxioCamIm03"]

        dir_path_str: int = CommonUtil.obtain_project_default_input_dir_path() + "asm3/"


        for image_name in image_name_list:
            original_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_image(image_name, dir_path=dir_path_str)
            threshold_img = ImageUtil.obtain_threshold_image(original_img);             ImageUtil.show_image_in_dip_view(threshold_img, title="threshold_img")

            segment_size: int = 9
            se_shape: str = "rectangular"
            top_hat_img = ImageUtil.white_top_hat(threshold_img, segment_size, se_shape)

            ImageUtil.show_image_in_dip_view(top_hat_img, title="top_hat_img")



    @staticmethod
    def test_threshold():
        image_name_list: list = ["rect3"]

        dir_path_str: int = CommonUtil.obtain_project_default_input_dir_path()

        for image_name in image_name_list:
            original_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_image(image_name, dir_path=dir_path_str)

            threshold_img_1 = ImageUtil.obtain_threshold_image(original_img)
            ImageUtil.show_image_in_dip_view(threshold_img_1, title="threshold_img_1")

#
# # filter_img = dip.Gauss(dip_img)
# # OD = ~dip.Threshold(filter_img)[0];             ImageUtil.show_image_in_dip_view(OD, title="Threshold(filter_img")
#             original_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_image(image_name, dir_path=dir_path_str)
#             gauss_img = original_img #ImageUtil.gauss_filter(original_img, 1)
#             threshold_img_2 = ~ImageUtil.obtain_threshold_image_trial(gauss_img)
#             ImageUtil.show_image_in_dip_view(threshold_img_2, title="threshold_img_2")
#
#
#
#
#
#             input_file_dir: str = CommonUtil.obtain_project_default_input_dir_path() + "calibrate_test/"
#             png_file_name: str = "circle.png"
#             tif_file_name: str = "circle.tif"
#
# # dip.Threshold(filter_img)[0]
#             dip_img = ImageUtil.obtain_image(tif_file_name, input_file_dir)
#             threshold_img_3 = ~ImageUtil.obtain_threshold_image_trial(dip_img)
#             ImageUtil.show_image_in_dip_view(threshold_img_3, title="threshold_img_3")



    @staticmethod
    def erosion_test1():
        image_name_list: list = ["AxioCamIm01", "AxioCamIm02", "AxioCamIm03"]

        dir_path_str: int = CommonUtil.obtain_project_default_input_dir_path() + "asm3/"
        image_name: str = ""

        for image_name in image_name_list:
            original_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_image(image_name, dir_path=dir_path_str)
            threshold_img = ImageUtil.obtain_threshold_image(original_img)

            segment_size: int = 9
            erosion_img = ImageUtil.erosion(threshold_img, segment_size, se_shape="rectangular")

            ImageUtil.show_image_in_dip_view(erosion_img, title="image_name")




    @staticmethod
    def erosion_test():
        image_name_list: list = ["AxioCamIm01", "AxioCamIm02", "AxioCamIm03"]

        dir_path_str: int = CommonUtil.obtain_project_default_input_dir_path() + "asm3/"
        image_name: str = ""

        for image_name in image_name_list:
            original_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_image(image_name, dir_path=dir_path_str)
            threshold_img = ImageUtil.obtain_threshold_image(original_img)

            segment_size: int = 9
            erosion_img = ImageUtil.erosion(threshold_img, segment_size)

            ImageUtil.show_image_in_dip_view(erosion_img)