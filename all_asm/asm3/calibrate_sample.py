import pprint

import numpy as np
import diplib as dip
import pandas as pd
import cv2

from util.common_util import CommonUtil
from util.image_util import ImageUtil


# https://github.com/DIPlib/diplib/issues/10
if __name__ == '__main__':

    input_file_dir: str = CommonUtil.obtain_project_default_input_dir_path() + "calibrate_test/"
    png_file_name: str = "circle.png"
    tif_file_name: str = "circle.tif"


    """
    I am using 3 appraches to measure the Diameter of the holes
    
    1) Using Mean radius returned by 'Radius'
    2) Mean of the axes returned by 'Dimensional Ellipsoid' 
    3) Using Area 'Size' to calculate the Diameter
    
    """

    dip_img = dip.Image(cv2.imread(input_file_dir + png_file_name, 0))
    # dip_img = ImageUtil.obtain_image(tif_file_name, input_file_dir)

    # ImageUtil.gauss_filter
    # ImageUtil.threshold
    filter_img = dip.Gauss(dip_img)
    OD = ~dip.Threshold(filter_img)[0];             ImageUtil.show_image_in_dip_view(OD, title="Threshold(filter_img")
    OD = dip.EdgeObjectsRemove(OD);                 ImageUtil.show_image_in_dip_view(OD, title="OD EdgeObjectsRemove")
    OD = dip.Opening(dip.Closing(OD, 9), 9);        ImageUtil.show_image_in_dip_view(OD, title="Opening(dip.Closing")
    ImageUtil.show_image_in_dip_view(~OD, title=" ~OD")
    ID = dip.EdgeObjectsRemove(~OD);                ImageUtil.show_image_in_dip_view(ID, title=" EdgeObjectsRemove")

    #label the images
    lab_OD = dip.Label(OD, minSize=10000);                ImageUtil.show_image_in_dip_view(lab_OD, title="lab_OD")
    lab_ID = dip.Label(ID, minSize=1000, maxSize=30000);  ImageUtil.show_image_in_dip_view(lab_ID, title="lab_ID")

    #Measurement
    msr_OD = dip.MeasurementTool.Measure(lab_OD, dip_img, ['Radius', 'Center', 'Inertia', 'DimensionsEllipsoid', 'Size'])
    msr_ID = dip.MeasurementTool.Measure(lab_ID, dip_img, ['Radius', 'Center', 'Inertia', 'DimensionsEllipsoid', 'Size'])



    # a placeholder dataframe to hold the result
    df = pd.DataFrame(columns=['feature','maxD','meanD','minD','center','axis_x','axis_y','mean_axis','size','dia_measured_from_size'])

    # add OD values
    df.loc[0] = 'OD', \
                msr_OD[1]['Radius'][0]*2, \
                msr_OD[1]['Radius'][1]*2, \
                msr_OD[1]['Radius'][2]*2, \
                tuple(msr_OD[1]['Center']), \
                msr_OD[1]['DimensionsEllipsoid'][0], \
                msr_OD[1]['DimensionsEllipsoid'][1], \
                (msr_OD[1]['DimensionsEllipsoid'][0] + msr_OD[1]['DimensionsEllipsoid'][1])/2, \
                msr_OD[1]['Size'][0], \
                2*np.sqrt(msr_OD[1]['Size'][0] / np.pi)

    # add values for 4 PCD holes
    object_ids = msr_ID.Objects()
    for i in object_ids:
        df.loc[i] = 'hole_{}'.format(i),msr_ID[i]['Radius'][0]*2,msr_ID[i]['Radius'][1]*2,msr_ID[i]['Radius'][2]*2,tuple(msr_ID[i]['Center']),msr_ID[i]['DimensionsEllipsoid'][0],msr_ID[i]['DimensionsEllipsoid'][1],(msr_ID[i]['DimensionsEllipsoid'][0]+msr_ID[i]['DimensionsEllipsoid'][1])/2,msr_ID[i]['Size'][0],2*np.sqrt(msr_ID[i]['Size'][0] / np.pi)

    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(df)


    CommonUtil.press_enter_to_continue()