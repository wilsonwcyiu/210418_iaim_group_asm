import diplib as dip
import numpy as np
import time
import matplotlib.pyplot as plt
from scipy import stats


def getstatistics(values):
    print("Maximum value is " + str(values.max()))
    print("Minimum value is " + str(values.min()))
    print("Average is " + str(values.mean()))
    print("Mode is " + str(stats.mode(values)[0]))


def getpixelvalues(img):
    pixelValues = np.array([])

    for pixelLocation in range(len(img)):
        listElement = img[pixelLocation]
        pixelValues = np.append(pixelValues, int(listElement[0]))

    return pixelValues


def processimage():
    # Read image
    rect = dip.ImageReadTIFF("C:/Users/rosa-/PycharmProjects/iaim_own_work/images_assignment2/rect1b.tif")

    new_rect = dip.Gauss(rect, 4)

    #showimage(new_rect)

    # Reduce noise filter 1
    #rect = dip.MedianFilter(rect, "rectangular")
    # Reduce noise filter 2
    #rect = dip.Gauss(rect, 4)

    #Get threshold
    _, thresh = dip.Threshold(new_rect)
    print(thresh)

    rectbin = new_rect < thresh

    showimage(new_rect)

    #showimage(rectbin)

    #values = getpixelvalues(rect)
    #getstatistics(values)

    #rectbin = dip.Label(rectbin)
    #showimage(rectbin)
    #m = dip.MeasurementTool.Measure(rectbin, rect, ['Size', 'Perimeter'])
    #print(m)


def showimage(img):
    #dip.PyDIPviewer.Show(img)
    sleep_sec: int = 10
    img.Show()
    time.sleep(sleep_sec)
    return 0


processimage()