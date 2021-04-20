import time

import diplib
import numpy as np



import diplib as dip
from PIL import Image as PilImage
import PIL
from diplib import PyDIPjavaio




def measure_size_and_perimeter(image: PyDIPjavaio.ImageRead):
    iso_threshold: int = 65
    rectangles = image < iso_threshold
    rectangles = dip.Label(rectangles)

    px_measure: diplib.PyDIP_bin.MeasurementTool.Measurement = dip.MeasurementTool.Measure(rectangles, image, ['Size', 'Perimeter'])


    print("px_measure: ", type(px_measure), px_measure)

    size_list = np.array(px_measure['Size']).transpose()
    perimeter_list = np.array(px_measure['Perimeter']).transpose()

    return size_list, perimeter_list




# test
if __name__ == '__main__':
    print("starting...")
    sleep_sec: int = 3
    time.sleep(sleep_sec)
    image_file_path = "../../image_files/rect2"

    img: PyDIPjavaio.ImageRead = dip.ImageRead(image_file_path)
    # img.Show()
    dip.Show(img)
    time.sleep(sleep_sec)

    size, perimeter = measure_size_and_perimeter(img)
    print("size, perimeter ", size, perimeter)




    # https://drive.google.com/file/d/1Z5pyJS_lpJXuL92WgrgeE0YEufp2o2PP/view?usp=sharing -> https://drive.google.com/uc?id=1Z5pyJS_lpJXuL92WgrgeE0YEufp2o2PP
    # g_drive_url = "https://drive.google.com/uc?id=1Z5pyJS_lpJXuL92WgrgeE0YEufp2o2PP"
    # response = requests.get(g_drive_url)
    # image_bytes = io.BytesIO(response.content)
    # img = PIL.Image.open(image_bytes)
    # img.show()


    # img: dip.PyDIP_bin.Image = dip.ImageReadTIFF('D:/Wilson/google_drive/leiden_university_course_materials/bioinformatics/image_signal_processing_with_microscopy/2020 Assignment02 Images/rect1.tif')
    #
    # img.Show()
    # time.sleep(sleep_sec)
    #
    #
    #
    #
    # img: dip.PyDIP_bin.Image = dip.ImageReadTIFF('D:/Wilson/google_drive/leiden_university_course_materials/bioinformatics/image_signal_processing_with_microscopy/2020 Assignment02 Images/rect1.tif')
    # img.Show()
    #
    #
    #
    # # By default, the image intensities are mapped to the full display range (i.e. the minimum image intensity is black and the maximum is white). This can be changed for example as follows:
    # img1: dip.PyDIP_bin.Image = dip.ImageReadTIFF('D:/Wilson/google_drive/leiden_university_course_materials/bioinformatics/image_signal_processing_with_microscopy/2020 Assignment02 Images/rect1.tif')
    # print("unit")
    # img1.Show('unit')  # maps [0,1] to the display range
    # time.sleep(sleep_sec)
    #
    #
    # img2: dip.PyDIP_bin.Image = dip.ImageReadTIFF('D:/Wilson/google_drive/leiden_university_course_materials/bioinformatics/image_signal_processing_with_microscopy/2020 Assignment02 Images/rect1.tif')
    # print("8bit")
    # img2.Show('8bit')  # maps [0,255] to the display range
    # time.sleep(sleep_sec)
    #
    #
    # img: dip.PyDIP_bin.Image = dip.ImageReadTIFF('D:/Wilson/google_drive/leiden_university_course_materials/bioinformatics/image_signal_processing_with_microscopy/2020 Assignment02 Images/rect1.tif')
    # print("orientation")
    # img.Show('orientation')  # maps [0,pi] to the display range
    # time.sleep(sleep_sec)

    # img: diplib.PyDIP_bin.Image = dip.ImageReadTIFF('D:/Wilson/google_drive/leiden_university_course_materials/bioinformatics/image_signal_processing_with_microscopy/2020 Assignment02 Images/rect1.tif')
    # print("base")
    # img.Show('base')  # keeps 0 to the middle grey level, and uses a divergent color map
    # time.sleep(sleep_sec)
    #
    # img: diplib.PyDIP_bin.Image = dip.ImageReadTIFF('D:/Wilson/google_drive/leiden_university_course_materials/bioinformatics/image_signal_processing_with_microscopy/2020 Assignment02 Images/rect1.tif')
    # print("log")
    # img.Show('log')  # uses logarithmic mapping


    print("end")

    # input("Press enter to end the process...")