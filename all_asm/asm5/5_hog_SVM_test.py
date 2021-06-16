# Compute the HOG feature vector for all of your images and store these in one comma separated file – for cell sizes use 16 and 64, resulting in two sets.
import PIL
import diplib
import csv

from pandas import DataFrame

from util.common_util import CommonUtil
from util.image_util import ImageUtil
from util.plot_util import PlotUtil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import os
#importing required libraries
from skimage.io import imread
from skimage.transform import resize
from skimage.feature import hog
from skimage import exposure
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
import seaborn as sns

#Import svm model
from sklearn import svm
import pandas as pd

# https://www.datacamp.com/community/tutorials/svm-classification-scikit-learn-python
if __name__ == '__main__':


    # Configure files and directories
    input_dir: str = CommonUtil.obtain_project_default_input_dir_path() + 'asm5/'
    proj_output_dir_path: str = '../../file_output/'
    img_extension: str = ""

    file_name: str = "hog_black_64.csv"
    file_path: str = CommonUtil.join_path(input_dir, file_name)
    data_df: DataFrame = CommonUtil.read_csv_file(file_path)

    # data_df[0]
    print(data_df)
    print(data_df.iloc[0:3, 0:4])

    CommonUtil.press_enter_to_exit()



    x_input_train_list = [[1], [2], [3], [4], [5], [6], [7], [8]]
    y_output_train_result = [1, 1, 2, 2, 3, 3, 4, 4]


    # https://medium.com/all-things-ai/in-depth-parameter-tuning-for-svc-758215394769
    classifier = svm.SVC(kernel='linear')      # kernal_list: list = ['linear', 'rbf', 'poly']

    #Train the model using the training sets
    classifier.fit(x_input_train_list, y_output_train_result)

    #Predict the response for test dataset
    x_input_test_list = [[1], [1], [6], [6], [8], [8]]
    y_output_test_pred = classifier.predict(x_input_test_list)

    print(y_output_test_pred)
