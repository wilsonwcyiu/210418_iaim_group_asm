import diplib
import numpy
from diplib import PyDIPjavaio


class ImageUtil:


    def measure_size_and_perimeter(image: PyDIPjavaio.ImageRead):
        iso_threshold: int = 65
        rectangles = image < iso_threshold
        rectangles = diplib.Label(rectangles)

        px_measure: diplib.PyDIP_bin.MeasurementTool.Measurement = diplib.MeasurementTool.Measure(rectangles, image, ['Size', 'Perimeter'])


        print("px_measure: ", type(px_measure), px_measure)

        size_list = np.array(px_measure['Size']).transpose()
        perimeter_list = numpy.array(px_measure['Perimeter']).transpose()

        return size_list, perimeter_list
