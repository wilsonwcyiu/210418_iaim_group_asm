from diplib import PyDIPjavaio

from util.common_util import CommonUtil
from util.image_util import ImageUtil


if __name__ == '__main__':
    print("starting...")
    sleep_sec: int = 0

    file_name: str = "asm3/AxioCamIm01"
    img = ImageUtil.obtain_image(file_name)
    ImageUtil.show_image_in_dip_view(img)



    print("end")
    CommonUtil.press_enter_to_continue()
