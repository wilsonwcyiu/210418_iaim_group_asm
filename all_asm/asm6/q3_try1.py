import dip as dip
import diplib
from diplib import PyDIPjavaio

from util.common_util import CommonUtil
from util.image_util import ImageUtil
from util.plot_util import PlotUtil

if __name__ == '__main__':

    # Configure files and directories
    input_dir: str = CommonUtil.obtain_project_default_input_dir_path() + 'asm6/'
    proj_output_dir_path: str = CommonUtil.obtain_project_default_output_dir_path() + CommonUtil.generate_date_time_str() + "/"




    image_name_list: list = ["CHROMO3D.ics"]

    for image_name in image_name_list:
        curr_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_diplib_image(image_name, input_dir)


        # DataType : # https://diplib.org/diplib-docs/pixeltypes.html
        curr_img = diplib.Convert(curr_img, "UINT8")

        # print(curr_img(1,1,1))

        # pixel_value_list = ImageUtil.obtain_pixel_value_list(curr_img)
        # plot = PlotUtil.create_histogram_plot(pixel_value_list)
        # plot.show()

        # data_type = dip::DT_UINT8
        # diplib.Convert(curr_img, dt=)

        ImageUtil.show_image_in_dip_view(curr_img)


    CommonUtil.press_enter_to_exit()