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


def load_data(img_group:str):
    # Configure files and directories and settings
    input_dir: str = CommonUtil.obtain_project_default_input_dir_path() + 'asm5/'
    proj_dir_path: str = '../../file_output/'

    # reading the csv files for classification
    data_hog_16 = pd.read_csv(proj_dir_path + 'asm5/' + 'hog' + '_' + img_group + '_' + str(16) + '.csv')
    data_hog_64 = pd.read_csv(proj_dir_path + 'asm5/' + 'hog' + '_' + img_group + '_' + str(64) + '.csv')
    data_hue_size = pd.read_csv(proj_dir_path + 'asm5/' + 'measurement' + '_' + img_group + '.csv')

    data = pd.concat([data_hue_size, data_hog_16, data_hog_64], axis=1)

    return data


def combined_SVM(plotting: bool = False):
    # Configure files and directories and settings
    input_dir: str = CommonUtil.obtain_project_default_input_dir_path() + 'asm5/'
    proj_dir_path: str = '../../file_output/'


    data_white = load_data('white')
    data_white = data_white.loc[:, ~data_white.columns.duplicated()]
    # print(data_white.head())
    # print(data_white.shape)

    data_black = load_data('black')
    data_black = data_black.loc[:, ~data_black.columns.duplicated()]
    # print(data_black.head())
    print(data_black.shape)

    test_a = []
    train_a = []
    ripening_level = [1, 2, 3, 4]
    for level in ripening_level:
        chosen_white_data = data_white.loc[data_white['Label'] == level]
        X_white = chosen_white_data.drop(columns=['Label'])
        # label white is 1
        y_white = pd.DataFrame([1 for i in range(X_white.shape[0])], columns=['Label'])

        chosen_black_data = data_black.loc[data_black['Label'] == level]
        X_black = chosen_black_data.drop(columns=['Label'])
        # label black is 2
        y_black = pd.DataFrame([2 for i in range(X_black.shape[0])], columns=['Label'])


        X = pd.concat([X_white, X_black], axis=0)
        y = pd.concat([y_white, y_black], axis=0)
        print(y.shape)
        print(X.shape)

        # splitting the dataset on train and text set
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=level, shuffle=True)

        # crate a svm classifier
        # svm = svm.SVC(kernel='linear')
        svc = svm.SVC(kernel='linear')

        # train the model on the train set
        svc.fit(X_train, y_train)

        # predict the response for test and train dataset
        y_pred_test = svc.predict(X_test)
        y_pred_train = svc.predict(X_train)

        # computing accuracy and f1 score
        train_accuracy = accuracy_score(y_train, y_pred_train)
        # print("Train accuracy: ", train_accuracy)
        test_accuracy = accuracy_score(y_test, y_pred_test)
        # print("Test accuracy: ", test_accuracy)
        train_f1 = f1_score(y_train, y_pred_train, average='weighted')
        # print("Train f1 score: ", train_f1)
        test_f1 = f1_score(y_test, y_pred_test, average='weighted')
        # print("Test f1 score: ", test_f1)

        train_a.append(train_accuracy)
        test_a.append(test_accuracy)

        if plotting:
            # create confusion matrix for train and test set
            train_conf_matrix = confusion_matrix(y_train, y_pred_train)
            test_conf_matrix = confusion_matrix(y_test, y_pred_test)

            # figure of train confusion matrix
            sns.heatmap(train_conf_matrix, annot=True, fmt=".3f", linewidths=.5, square=True, cmap='Blues_r', annot_kws={"size": 15})
            plt.ylabel('Actual label', fontsize=15)
            plt.xlabel('Predicted label', fontsize=15)
            PlotUtil.save_plot_to_project_folder(plt, 'asm5', 'ripening_' + str(level) + '_train_conf_mat.png')
            # plt.show()
            plt.clf()

            # figure of test confusion matrix
            sns.heatmap(test_conf_matrix, annot=True, fmt=".3f", linewidths=.5, square=True, cmap='Blues_r', annot_kws={"size": 15})
            plt.ylabel('Actual label', fontsize=15)
            plt.xlabel('Predicted label', fontsize=15)
            PlotUtil.save_plot_to_project_folder(plt, 'asm5', 'ripening_' + str(level) + '_test_conf_mat.png')
            # plt.show()
            plt.clf()


    return train_a, test_a, ripening_level




if __name__ == '__main__':

    # Configure files and directories and settings
    input_dir: str = CommonUtil.obtain_project_default_input_dir_path() + 'asm5/'
    proj_dir_path: str = '../../file_output/'
    img_group: str = 'white'  # white / black


    # SVM for all combined features
    # run the SVM classification in one function
    # returns train and test accuracy
    train_accuracies, test_accuracies, labels = combined_SVM(plotting=True)

    # Plotting
    # set width of bar
    barWidth = 0.25

    # Set position of bar on X axis
    br1 = np.arange(len(train_accuracies))
    br2 = [x + barWidth for x in br1]

    # Make the plot
    plt.bar(br1, train_accuracies, color='g', width=barWidth,
            edgecolor='grey', label='train accuracy')
    plt.bar(br2, test_accuracies, color='b', width=barWidth,
            edgecolor='grey', label='test accuracy')

    # Adding Xticks
    plt.xlabel('Level of ripening', fontsize=15)
    plt.ylabel('Accuracy', fontsize=15)
    plt.xticks([r + barWidth for r in range(len(train_accuracies))],
               [str(i) for i in labels])

    plt.legend()
    # plt.show()
    PlotUtil.save_plot_to_project_folder(plt, 'asm5', 'ripening_levels_accuracies.png')
    plt.clf()











