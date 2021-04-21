# contributions of all team members used and combined:

import diplib
import numpy as np

import diplib as dip
from PIL import Image as PilImage
import PIL
from diplib import PyDIPjavaio

import matplotlib.pyplot as plt

from util import UtilFunctions



def measure_size_and_perimeter(img):
    threshold_value = UtilFunctions.threshold(img)
    # Segment image
    segm_img = img < threshold_value

    # Opening (erosion for removing smaller objects then dilation for restoring remaining objects)
    #segm_img = dip.BinaryOpening(segm_img, -1, 4)
    #segm_img = dip.BinaryDilation(segm_img)

    UtilFunctions.show_image_in_dip_view(segm_img, 4)

    # Label segmented objects
    segm_img = dip.Label(segm_img)

    # Get measurements
    px_measurements = dip.MeasurementTool.Measure(segm_img, img, ['Size', 'Perimeter'])
    print(px_measurements)

    # Get array with all sizes
    sizes = np.array(px_measurements['Size']).transpose()
    perimeters = np.array(px_measurements['Perimeter']).transpose()

    return sizes, perimeters


def plot_relative_discretization_error(mean_array, std_array, label, img_series):
    # Values for x-axis
    sqrt_mean = np.sqrt(mean_array)
    # Values for y-axis
    cv = std_array/mean_array

    fig, ax = plt.subplots()
    ax.plot(sqrt_mean, cv)

    ax.set(xlabel='square root of the mean',
           ylabel='coefficient of variation',
           title='The relative discretization error of '+label)
    fig.savefig("../plot_output/" + label + "_" + img_series)


if __name__ == '__main__':
    sleep_sec: int = 3

    # Initialize and state image name lists
    image_name_list: list = []
    image_name_list_noise: list = ["rect4b"]

    # Initialize parameters for Gaussian filter
    gauss_parameter_list = [3]

    # Initialize parameters for Median filter and then repeat steps
    median_parameter_list = ['elliptic']

    # Initialize statistic arrays
    mean_size = []
    std_size = []
    mean_perimeter = []
    std_perimeter = []

    # Performing analysis on no noise images
    for image_name in image_name_list:
        # Load current image
        curr_img = obtain_image(image_name)
        # Measure size and perimeter of current image
        sizes, perimeters = measure_size_and_perimeter(curr_img)

        # Get statistics
        mean, std = UtilFunctions.get_mean_std(sizes)
        mean_size.append(mean)
        std_size.append(std)
        print("Size:  | mean    ", mean, " | std    ", std, "  |")

        mean, std = UtilFunctions.get_mean_std(perimeters)
        mean_perimeter.append(mean)
        std_perimeter.append(std)
        print("Perimeter:  | mean    ", mean, "  | std    ", std, "  |")

    # Now, all the mean and std values are known for images (rect)1-4 that are used for the following:
    # Plot the graph of the relative discretization error of the size
    #plot_relative_discretization_error(np.array(mean_size), np.array(std_size), 'size', 'no_noise')
    # Plot the graph of the relative discretization error of the perimeter
    #plot_relative_discretization_error(np.array(mean_perimeter), np.array(std_perimeter), 'perimeter', 'no_noise')

    # Initialize date and time
    date_time_str = UtilFunctions.generate_date_time_str()

    '''
    for image_name in image_name_list_noise:
        # Load current image
        curr_img = UtilFunctions.obtain_image(image_name)
        # Apply Gaussian filter with different parameters
        for gauss_parameter_value in gauss_parameter_list:
            curr_gauss_img = dip.Gauss(curr_img, gauss_parameter_value)
            file_name = date_time_str + image_name + "_gauss_" + str(gauss_parameter_value)
            print(file_name)
            UtilFunctions.show_image_in_dip_view(curr_gauss_img, sleep_sec)
            # Here, also measure size and perimeter per image and per Gaussian filter with certain filter (for part 2.3, question 7)
            sizes, perimeters = measure_size_and_perimeter(curr_gauss_img)

            # Filters all irrelevant objects from incorrect segmentations
            UtilFunctions.print_largest_measurements(sizes[0], perimeters[0])

            # Then, get the statistics (mean and std) from these measurements
            mean, std = UtilFunctions.get_mean_std(sizes)
            mean_size.append(mean)
            std_size.append(std)
            print("Size:  | mean    ", mean, " | std    ", std, "  |")

            mean, std = UtilFunctions.get_mean_std(perimeters)
            mean_perimeter.append(mean)
            std_perimeter.append(std)
            print("Perimeter:  | mean    ", mean, "  | std    ", std, "  |")

    '''

    for image_name in image_name_list_noise:
        # Load current image
        curr_img = UtilFunctions.obtain_image(image_name)
        # Apply Gaussian filter with different parameters
        for median_parameter in median_parameter_list:
            curr_median_img = dip.MedianFilter(curr_img, median_parameter)
            file_name = date_time_str + image_name + "_median_" + str(median_parameter)
            print(file_name)
            UtilFunctions.show_image_in_dip_view(curr_median_img, sleep_sec)
            # Here, also measure size and perimeter per image and per Gaussian filter with certain filter (for part 2.3, question 7)
            sizes, perimeters = measure_size_and_perimeter(curr_median_img)

            # Filters all irrelevant objects from incorrect segmentations
            UtilFunctions.print_largest_measurements(sizes[0], perimeters[0])

            # Then, get the statistics (mean and std) from these measurements
            mean, std = UtilFunctions.get_mean_std(sizes)
            mean_size.append(mean)
            std_size.append(std)
            print("Size:  | mean    ", mean, " | std    ", std, "  |")

            mean, std = UtilFunctions.get_mean_std(perimeters)
            mean_perimeter.append(mean)
            std_perimeter.append(std)
            print("Perimeter:  | mean    ", mean, "  | std    ", std, "  |")


    # Now, all the mean and std values are known for images (rect)1a,1b-4a,4b that are used for the following:
    # Plot the relative discretization error graphs for size and perimeter where FOR EACH label (size and perimeter):
    # FIRST graph shows values from images 1a-4a with first Gaussian filter, 
    # where the SECOND graph shows values from images 1a-4a with second Gaussian filter, where
    # THIRD graph shows values from images 1b-4b with first Gaussian filter and where FOURTH graph shows values from
    # images 1b-4b with second Gaussian filter
    
    # SIGNAL TO NOISE RATIO
    # -> Characterizes image quality. mean_sig/std_sig where mean_sig is average signal value and std_sig is std of the signal
    # Do this without noise suppression filter:
        # First series: rect1, rect2, rect3, rect4
        # Second series: rect1a, rect2a, rect3a, rect4a
        # Third series: rect1b, rect2b, rect3b, rect4b
        # Put the results in a table
    # Do this with best performing noise suppression filter:
        # First series: rect1, rect2, rect3, rect4
        # Second series: rect1a, rect2a, rect3a, rect4a
        # Third series: rect1b, rect2b, rect3b, rect4b
        # Put the results in a table
    
    # Lastly, produce plot (with SNR against sum of all measurements in that image) PER image