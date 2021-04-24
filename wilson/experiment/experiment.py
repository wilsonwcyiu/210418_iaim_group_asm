import diplib
import numpy as np

from diplib import PyDIPjavaio

from util.common_util import CommonUtil
from util.image_util import ImageUtil


def measure_size_and_perimeter(image: PyDIPjavaio.ImageRead):
    iso_threshold: int = 65
    rectangles = image < iso_threshold
    rectangles = diplib.Label(rectangles)

    px_measure: diplib.PyDIP_bin.MeasurementTool.Measurement = diplib.MeasurementTool.Measure(rectangles, image, ['Size', 'Perimeter'])


    print("px_measure: ", type(px_measure), px_measure)

    size_list = np.array(px_measure['Size']).transpose()
    perimeter_list = np.array(px_measure['Perimeter']).transpose()

    return size_list, perimeter_list




# test
if __name__ == '__main__':
    print("starting...")
    sleep_sec: int = 0

    image_name_list: list = ["rect1a", "rect1b", "rect2a", "rect2b", "rect3a", "rect3b", "rect4a", "rect4b"]
    guass_value_list: list = [2,5]

    date_time_str: str = CommonUtil.generate_date_time_str()
    for image_name in image_name_list:
        tmp_img: PyDIPjavaio.ImageRead = ImageUtil.obtain_image(image_name)

        for guass_value in guass_value_list:
            sigmas: int = guass_value

            filtered_img = ImageUtil.gauss_filter(tmp_img, sigmas)

            file_name = image_name + "_guass_filter_" + str(guass_value) + ".tiff"

            CommonUtil.save_image_to_default_project_folder(img=filtered_img, dir_name=date_time_str, file_name=file_name)

            # ImageUtil.show_image_in_dip_view(filtered_img, sleep_sec)

















    # img.Show()
    # dip.Show(img)
    # time.sleep(sleep_sec)
    #
    #
    # size, perimeter = ImageUtil.measure_size_and_perimeter(image=img, iso_threshold=65)
    # print("size, perimeter ", size, perimeter)


    # new_rect = dip.Gauss(img, 2)
    # ImageUtil.show_image_in_dip_view(new_rect, sleep_sec)


    # new_rect = dip.Gauss(img, 3)
    # ImageUtil.show_image_in_dip_view(new_rect, sleep_sec)
    #
    #
    # new_rect = dip.Gauss(img, 4)
    # ImageUtil.show_image_in_dip_view(new_rect, sleep_sec)


    # new_rect = dip.Gauss(img, 2)
    # new_rect.Show()
    # CommonUtil.sleep(sleep_sec)
    #
    #
    # new_rect = dip.Gauss(img, 3)
    # new_rect.Show()
    # CommonUtil.sleep(sleep_sec)
    #
    #
    # new_rect = dip.Gauss(img, 4)
    # new_rect.Show()
    # CommonUtil.sleep(sleep_sec)

    # showimage(new_rect)
    # _, thresh = dip.Threshold(rect) -> 64.5



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