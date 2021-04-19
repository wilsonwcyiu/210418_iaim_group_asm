import time

import diplib
import diplib as dip

# test
if __name__ == '__main__':
    print("starting...")
    sleep_sec: int = 5

    img: diplib.PyDIP_bin.Image = dip.ImageReadTIFF('D:/Wilson/google_drive/leiden_university_course_materials/bioinformatics/image_signal_processing_with_microscopy/2020 Assignment02 Images/rect1.tif')
    assert(img, diplib.PyDIP_bin.Image)



    img.Show()


    # By default, the image intensities are mapped to the full display range (i.e. the minimum image intensity is black and the maximum is white). This can be changed for example as follows:
    img: diplib.PyDIP_bin.Image = dip.ImageReadTIFF('D:/Wilson/google_drive/leiden_university_course_materials/bioinformatics/image_signal_processing_with_microscopy/2020 Assignment02 Images/rect1.tif')

    print("unit")
    img.Show('unit')  # maps [0,1] to the display range
    time.sleep(sleep_sec)


    img: diplib.PyDIP_bin.Image = dip.ImageReadTIFF('D:/Wilson/google_drive/leiden_university_course_materials/bioinformatics/image_signal_processing_with_microscopy/2020 Assignment02 Images/rect1.tif')

    print("8bit")
    img.Show('8bit')  # maps [0,255] to the display range
    time.sleep(sleep_sec)

    print("orientation")
    img.Show('orientation')  # maps [0,pi] to the display range
    time.sleep(sleep_sec)

    print("base")
    img.Show('base')  # keeps 0 to the middle grey level, and uses a divergent color map
    time.sleep(sleep_sec)

    print("log")
    img.Show('log')  # uses logarithmic mapping


    print("end")

    input("Press enter to end the process...")