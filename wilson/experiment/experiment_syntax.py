import os

import diplib
import numpy as np

from diplib import PyDIPjavaio
from diplib.PyDIP_bin import SE
from matplotlib import pyplot

from util.common_util import CommonUtil
from util.image_util import ImageUtil





# test_case
if __name__ == '__main__':
    print("starting...")
    sleep_sec: int = 0

    data_tup = (0,1,2,3)
    print(len(data_tup))

    for i in range(0, 4):
        print(i)

    print("end")
    input("Press enter to end the process...")