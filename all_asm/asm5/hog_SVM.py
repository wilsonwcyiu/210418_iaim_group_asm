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


def write_csv_features(input_dir: str, proj_dir_path: str, feature:str, img_group: str, cell_size: int):

    first_line = True

    with open(proj_dir_path + 'asm5/' + feature + '_' + img_group + '_' + str(cell_size) + '.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=",")

        types: list = ['1', '2', '3', '4']  # [number]_[black/white] - number means sage of ripening
        for stage in types:
            file_list: list = CommonUtil.obtain_file_name_list(input_dir + stage + '_' + img_group + '/')
            for file in file_list:
                img_rgb = ImageUtil.obtain_image_rgb_array(input_dir + stage + '_' + img_group + '/' + file)
                img_gray = ImageUtil.obtain_image_gray_array(input_dir + stage + '_' + img_group + '/' + file)

                # resizing image to have same number of features for images of different size
                resized_img = resize(img_rgb, (128 * 4, 64 * 4))
                # plt.axis("off")
                # plt.imshow(resized_img)
                # print(resized_img.shape)

                # creating hog features for resized image
                fd, hog_image = hog(resized_img, orientations=8,
                                    pixels_per_cell=(cell_size, cell_size),
                                    cells_per_block=(1, 1), visualize=True, multichannel=True)

                if first_line:  # first line of a file is a header
                    header = ['Label'] + ['Feature '+str(i) for i in range(len(fd))]
                    # for i in range(len(fd)):
                    #     header.append("Feature "+str(i))
                    writer.writerow(header)
                    first_line = False

                # fd contains the features for classification
                # inserting stage of ripening on the first position of each line,
                # which serves as label for classification
                line = np.insert(fd, 0, int(stage))

                # writing to csv file
                writer.writerow(line)


def hog_SVM(img_group: str, cell_size: int, plotting: bool=False):
    # Configure files and directories and settings
    input_dir: str = CommonUtil.obtain_project_default_input_dir_path() + 'asm5/'
    proj_dir_path: str = '../../file_output/'
    feature: str = 'hog'

    # compute the HOG features and write them into csv file
    # write_csv_features(input_dir, proj_dir_path, feature, img_group, cell_size)

    # reading the csv file for classification
    data = pd.read_csv(proj_dir_path + 'asm5/' + feature + '_' + img_group + '_' + str(cell_size) + '.csv')
    print(data.head())

    # dividing the data on labels and features
    y = data['Label']
    X = data.drop(columns=['Label'])

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

    print("Image group:", img_group, "feature:", feature, "cell size:", cell_size)

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
        # plt.show()
        PlotUtil.save_plot_to_project_folder(plt, 'asm5', img_group + '_' + feature + '_' + str(cell_size) +'_train_conf_mat.png')
        plt.clf()

        # figure of test confusion matrix
        sns.heatmap(test_conf_matrix, annot=True, fmt=".3f", linewidths=.5, square=True, cmap='Blues_r')
        plt.ylabel('Actual label')
        plt.xlabel('Predicted label')
        # plt.show()
        PlotUtil.save_plot_to_project_folder(plt, 'asm5', img_group + '_' + feature + '_' + str(cell_size) +'_test_conf_mat.png')
        plt.clf()

    return train_accuracy, test_accuracy



if __name__ == '__main__':

    # Configure files and directories and settings
    input_dir: str = CommonUtil.obtain_project_default_input_dir_path() + 'asm5/'
    proj_dir_path: str = '../../file_output/'
    img_group: str = 'white'  # white / black
    cell_size: int = 16  # 16 / 64

    # compute the HOG features and write them into csv file
    # write_csv_features(input_dir, proj_dir_path, feature, img_group, cell_size)


    # SVM for HOG features
    # run the SVM classification in one function
    # returns train and test accuracy
    train_accuracy, test_accuracy = hog_SVM(img_group, cell_size, True)




