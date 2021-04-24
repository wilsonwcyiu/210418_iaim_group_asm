from util.common_util import CommonUtil


class UnderDevUtil():


    @staticmethod
    def print_variable_name_and_value(*args):
        raise Exception("not developed")
        txt: str = ""
        for arg in args:
            abbb = "1"
            name = CommonUtil.name_str(abbb, globals())
            print(name, ": ", abbb)



    # @staticmethod
    # def measure_size_and_perimeter(img):
    #     threshold_value = ImageUtil.threshold(img)
    #     # Segment image
    #     segm_img = img < threshold_value
    #
    #     # Opening (erosion for removing smaller objects then dilation for restoring remaining objects)
    #     #segm_img = dip.BinaryOpening(segm_img, -1, 4)
    #     #segm_img = dip.BinaryDilation(segm_img)
    #
    #     # Label segmented objects
    #     segm_img = diplib.Label(segm_img)
    #
    #     # Get measurements
    #     px_measurements = diplib.MeasurementTool.Measure(segm_img, img, ['Size', 'Perimeter'])
    #     #print(px_measurements)
    #
    #     # Get array with all sizes
    #     surface_area_list = np.array(px_measurements['Size']).transpose()
    #     perimeter_list = np.array(px_measurements['Perimeter']).transpose()
    #
    #     return surface_area_list, perimeter_list
