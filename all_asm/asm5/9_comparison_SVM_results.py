# Compute the HOG feature vector for all of your images and store these in one comma separated file – for cell sizes use 16 and 64, resulting in two sets.
import PIL
import diplib
import csv

from util.common_util import CommonUtil
from util.plot_util import PlotUtil
import numpy as np
import matplotlib.pyplot as plt


from combined_SVM import combined_SVM
from hue_shape_SVM import hue_SVM, shape_SVM
from hog_SVM import hog_SVM



if __name__ == '__main__':

    # Configure files and directories and settings
    input_dir: str = CommonUtil.obtain_project_default_input_dir_path() + 'asm5/'
    proj_dir_path: str = '../../file_output/'
    img_group: str = 'black'  # white / black

    labels = ['HOG_16', 'HOG_64', 'Hue', 'Shape', 'Combined']
    train_accuracies = []
    test_accuracies = []

    # SVM for all HOG features with cell size 16
    # returns train and test accuracy
    train_accuracy, test_accuracy = hog_SVM(img_group, 16, True)
    train_accuracies.append(train_accuracy)
    test_accuracies.append(test_accuracy)

    # SVM for all HOG features with cell size 64
    # returns train and test accuracy
    train_accuracy, test_accuracy = hog_SVM(img_group, 64, True)
    train_accuracies.append(train_accuracy)
    test_accuracies.append(test_accuracy)

    # SVM for Hue features
    # returns train and test accuracy
    train_accuracy, test_accuracy = hue_SVM(img_group, True)
    train_accuracies.append(train_accuracy)
    test_accuracies.append(test_accuracy)

    # SVM for Shape features
    # returns train and test accuracy
    train_accuracy, test_accuracy = shape_SVM(img_group, True)
    train_accuracies.append(train_accuracy)
    test_accuracies.append(test_accuracy)

    # SVM for all combined features
    # returns train and test accuracy
    train_accuracy, test_accuracy = combined_SVM(img_group, True)
    train_accuracies.append(train_accuracy)
    test_accuracies.append(test_accuracy)

    print("Labels:", labels)
    print("Train acc:", train_accuracies)
    print("Test acc:", test_accuracies)


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
    plt.xlabel('Features', fontsize=15)
    plt.ylabel('Accuracy',  fontsize=15)
    plt.xticks([r + barWidth for r in range(len(train_accuracies))],
               labels)

    plt.legend()
    # plt.show()
    PlotUtil.save_plot_to_project_folder(plt, 'asm5', img_group + '_accuracies_compared.png')
    plt.clf()













