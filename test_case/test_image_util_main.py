from test_case.test_image_util import TestImageUtil
from util.common_util import CommonUtil


if __name__ == '__main__':
    print("starting...")
    sleep_sec: int = 0

    TestImageUtil.top_hat_test1()

    # TestImageUtil.test_threshold()

    # TestImageUtil.erosion_test1()



    print("end")
    CommonUtil.press_enter_to_continue()