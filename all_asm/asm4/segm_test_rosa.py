import numpy as np
import diplib as dip
from diplib import PyDIPjavaio

from util.common_util import CommonUtil
from util.image_util import ImageUtil
from util.plot_util import PlotUtil

if __name__ == '__main__':
    input_dir: str = CommonUtil.obtain_project_default_input_dir_path() + "asm4/"

    image_series_names = ['MTLn3+EGF', 'MTLn3-ctrl']

    for image_series_name in image_series_names:
        for sequence in range(30):
            image_file_name = image_series_name + str(sequence).zfill(4) + '.png'
            curr_img = ImageUtil.obtain_image(image_file_name, input_dir)

            structuring_element = dip.PyDIP_bin.SE(shape='elliptic', param=10)
            curr_img = dip.Tophat(curr_img, structuring_element)

            structuring_element = dip.PyDIP_bin.SE(shape='elliptic', param=2)
            curr_img = dip.Closing(curr_img, structuring_element)

            file_name = image_file_name.replace('.png', '_processed.tif')
            CommonUtil.save_image_to_default_project_folder(curr_img, "asm4", file_name)

            segm_img = ImageUtil.segment_image_white(curr_img)
            segm_img = dip.BinaryOpening(segm_img)

            segm_img = dip.SmallObjectsRemove(segm_img, 100)

            file_name = image_file_name.replace('.png', '_segmented.tif')
            CommonUtil.save_image_to_default_project_folder(segm_img, "asm4", file_name)