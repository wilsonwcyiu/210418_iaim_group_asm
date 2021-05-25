# Segmentation of berry images

import PIL
import diplib
from diplib.PyDIP_bin import SE

from util.common_util import CommonUtil
from util.image_util import ImageUtil

from PIL import Image


if __name__ == '__main__':

    # Configure files and directories
    input_dir: str = CommonUtil.obtain_project_default_input_dir_path() + 'asm5/'
    proj_output_dir_path: str = '../../image_output/asm5'
    img_extension: str = ""

    folder_list: list = ["3_black"]

    for folder in folder_list:
        # To collect relative image paths of all images in folder
        img_relative_path_list: list = []


        # Output image directory
        output_dir_path: str = proj_output_dir_path + '/' + folder + '/'


        # ATM only first image of folder
        file_list: list = CommonUtil.obtain_file_name_list(input_dir + folder + "/")
        for file in file_list:
            img_relative_path_list.append(folder + "/" + file)

        # Go through every image
        for img_relative_path in img_relative_path_list:
            # TODO 46.Black_Mulberry_3 does not work?
            # Obtain berry label/name
            img_name: str = img_relative_path.split("/")[-1].replace('.jpg', '')

            # Load current image, img[location][RGB channel]
            curr_img: diplib.ImageRead = ImageUtil.obtain_diplib_image(img_relative_path, input_dir)


            # ---------- Pre-processing ----------


            # Obtain size of image
            width, height = curr_img.Sizes()

            # Create new image to save single channel values
            new_img = diplib.Image((width, height), 1)

            # Subtract red channel (0) values from blue channel (2) values
            for i in range(len(curr_img)):
                new_img[i] = curr_img[i][2] - curr_img[i][0]

            CommonUtil.save_image_to_folder(new_img, output_dir_path, img_name + '_processed.jpg')


            # ---------- Segmentation ----------


            segm_img: diplib.Image = ImageUtil.segment_image_black(new_img)

            CommonUtil.save_image_to_folder(segm_img, output_dir_path, img_name + '_segmented.tif')

            '''
            # Pre-processing
            gray_scale_img: diplib.Image = ImageUtil.convert_to_gray_scale(curr_img)

            ImageUtil.show_image_in_dip_view(gray_scale_img, 10, "gray-scale")

            structuring_element: SE = diplib.PyDIP_bin.SE(shape='elliptic', param=10)
            opening_img: diplib.Image = diplib.Opening(gray_scale_img, structuring_element)

            processed_img: diplib.Image = diplib.Gauss(opening_img, 18)

            ImageUtil.show_image_in_dip_view(processed_img, 3, "processed")

            line_detect: diplib.Image = diplib.FrangiVesselness(processed_img, 10, polarity="black")

            # segm_img: diplib.Image = ImageUtil.segment_image_white(line_detect)

            ImageUtil.show_image_in_dip_view(line_detect, 5, "end")

            '''
