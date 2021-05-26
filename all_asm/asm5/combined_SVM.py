# Compute the HOG feature vector for all of your images and store these in one comma separated file – for cell sizes use 16 and 64, resulting in two sets.
import PIL
import diplib
import csv

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



def combined_SVM(img_group: str, plotting: bool=False):
    # Configure files and directories and settings
    input_dir: str = CommonUtil.obtain_project_default_input_dir_path() + 'asm5/'
    proj_dir_path: str = '../../file_output/'


    # reading the csv files for classification
    data_hog_16 = pd.read_csv(proj_dir_path + 'asm5/' + 'hog' + '_' + img_group + '_' + str(16) + '.csv')
    data_hog_64 = pd.read_csv(proj_dir_path + 'asm5/' + 'hog' + '_' + img_group + '_' + str(64) + '.csv')
    data_hue_size = pd.read_csv(proj_dir_path + 'asm5/' + 'measurement' + '_' + img_group + '.csv')

    data = pd.concat([data_hue_size, data_hog_16, data_hog_64], axis=1)

    print(data.head())
    print(data.shape)

    # dividing the data on labels and features
    y = data['Label'].iloc[:, [0]]
    print(y.shape)
    X = data.drop(columns=['Label'])
    print(X.shape)
    # splitting the dataset on train and text set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1, shuffle=True)

    # crate a svm classifier
    # svm = svm.SVC(kernel='linear')
    svc = svm.SVC(kernel='linear')

    # train the model on the train set
    svc.fit(X_train, y_train)

    # predict the response for test and train dataset
    y_pred_test = svc.predict(X_test)
    y_pred_train = svc.predict(X_train)

    print("Image group:", img_group, "features: combined")

    # computing accuracy and f1 score
    train_accuracy = accuracy_score(y_train, y_pred_train)
    print("Train accuracy: ", train_accuracy)
    test_accuracy = accuracy_score(y_test, y_pred_test)
    print("Test accuracy: ", test_accuracy)
    train_f1 = f1_score(y_train, y_pred_train, average='weighted')
    print("Train f1 score: ", train_f1)
    test_f1 = f1_score(y_test, y_pred_test, average='weighted')
    print("Test f1 score: ", test_f1)

    if plotting:
        # create confusion matrix for train and test set
        train_conf_matrix = confusion_matrix(y_train, y_pred_train)
        test_conf_matrix = confusion_matrix(y_test, y_pred_test)

        # figure of train confusion matrix
        sns.heatmap(train_conf_matrix, annot=True, fmt=".3f", linewidths=.5, square=True, cmap='Blues_r')
        plt.ylabel('Actual label')
        plt.xlabel('Predicted label')
        PlotUtil.save_plot_to_project_folder(plt, 'asm5', img_group + '_combined_train_conf_mat.png')
        # plt.show()
        plt.clf()

        # figure of test confusion matrix
        sns.heatmap(test_conf_matrix, annot=True, fmt=".3f", linewidths=.5, square=True, cmap='Blues_r')
        plt.ylabel('Actual label')
        plt.xlabel('Predicted label')
        PlotUtil.save_plot_to_project_folder(plt, 'asm5', img_group + '_combined_test_conf_mat.png')
        # plt.show()
        plt.clf()

    return train_accuracy, test_accuracy



if __name__ == '__main__':

    # Configure files and directories and settings
    input_dir: str = CommonUtil.obtain_project_default_input_dir_path() + 'asm5/'
    proj_dir_path: str = '../../file_output/'
    img_group: str = 'white'  # white / black


    # SVM for all combined features
    # run the SVM classification in one function
    # returns train and test accuracy
    train_accuracy, test_accuracy = combined_SVM(img_group, plotting=True)











