# contributions of all team members used and combined:

import diplib
import numpy as np

import diplib as dip
from PIL import Image as PilImage
import PIL
from diplib import PyDIPjavaio

import matplotlib.pyplot as plt

from util import UtilFunctions


def measure_conv_and_solid(img):
    # Get threshold
    threshold_value = UtilFunctions.threshold(img)

    # Segment image
    segm_img = img < threshold_value

    #UtilFunctions.show_image_in_dip_view(segm_img, 4)

    # Label segmented objects
    segm_img = dip.Label(segm_img)

    # Get measurements
    measurements = dip.MeasurementTool.Measure(segm_img, img, ['Size', 'Solidity', 'Convexity'])

    sizes = []
    convexity = []
    solidity = []
    perimeters = []

    # Only save the measurement values of the actual objects; filter out the irrelevant objects and their measurements
    for object in np.array(measurements):
        if object[0] > 200:
            sizes.append(object[0])
            convexity.append(object[2])
            solidity.append(object[1])
            perimeters.append(object[4])

    return sizes, convexity, solidity, perimeters


def measure_size_and_perimeter(img):
    threshold_value = UtilFunctions.threshold(img)
    # Segment image
    segm_img = img < threshold_value

    # Opening (erosion for removing smaller objects then dilation for restoring remaining objects)
    #segm_img = dip.BinaryOpening(segm_img, -1, 4)
    #segm_img = dip.BinaryDilation(segm_img)

    # Label segmented objects
    segm_img = dip.Label(segm_img)

    # Get measurements
    px_measurements = dip.MeasurementTool.Measure(segm_img, img, ['Size', 'Perimeter'])
    #print(px_measurements)

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


def plot_snr_measurements(sizes, snr_values, image_names):
    labels = ['no noise series', 'A series']
    colors = ['tab:gray', 'tab:blue']

    sizes_per_series = [sizes[0:4], sizes[4:8]]
    snr_per_series = [snr_values[0:4], snr_values[4:8]]
    fig, ax = plt.subplots()

    for i in range(len(sizes_per_series)):
        x_values = np.log(sizes_per_series[i])
        y_values = snr_per_series[i]

        print(sizes_per_series[i])
        print(y_values)

        ax.scatter(x_values, y_values, c=colors[i], label=labels[i])

    ax.legend()

    ax.set(xlabel='log(total perimeter of objects in image)',
           ylabel='SNR value',
           title='SNR related to the perimeter')
    fig.savefig("../plot_output/snr_plot")


if __name__ == '__main__':
    sleep_sec: int = 3

    # Which images are going to be analysed?
    image_name_list: list = ["rect1", "rect2", "rect3", "rect4", "rect1a", "rect2a", "rect3a", "rect4a"]

    snr_values = []
    sum_sizes = []
    sum_perimeters = []

    for image_name in image_name_list:
        # Load image
        curr_img = UtilFunctions.obtain_image(image_name)

        # Get pixel values from current image
        pixel_values = UtilFunctions.get_pixel_values(curr_img)

        # Get average and std of the pixel values
        mean, std = UtilFunctions.get_mean_std(pixel_values)
        # Calculate SNR
        snr = mean / std
        snr_values.append(snr)

        # Calculate convexity and solidity
        sizes, convexity, solidity, perimeters = measure_conv_and_solid(curr_img)

        # Every entry in array corresponds to one object in image
        print('Sizes of ', image_name, ': ', sizes)
        print('Perimeters of ', image_name, ': ', perimeters)
        print('Convexity of ', image_name, ': ', convexity)
        print('Solidity of ', image_name, ': ', solidity)

        #norm_convexity_value = sum(convexity) / len(convexity)
        #norm_convexity.append(norm_convexity_value)

        sum_sizes.append(sum(sizes))
        sum_perimeters.append(sum(perimeters))


    #print(norm_convexity)
    #print(sum_sizes)

    plot_snr_measurements(sum_perimeters, snr_values, image_name_list)


    '''

    # Initialize and state image name lists
    image_name_list: list = ["rect1", "rect2", "rect3", "rect4", "rect1a", "rect2a", "rect3a", "rect4a", "rect1b", "rect2b", "rect3b", "rect4b"]
    image_name_list_no_noise: list = ["rect1", "rect2", "rect3", "rect4"]

    # Initialize parameters for Gaussian filter
    gauss_parameter_list = [2]

    # Initialize parameters for Median filter and then repeat steps
    median_parameter_list = ['elliptic']

    # Initialize statistic arrays
    mean_size = []
    std_size = []
    mean_perimeter = []
    std_perimeter = []

    # For storage of sizes and snr values of image series without noise and without filter
    size_values_no_filter = []
    snr_values_no_filter = []

    # Performing analysis on no noise images
    for image_name in image_name_list_no_noise:
        # Load current image
        curr_img = UtilFunctions.obtain_image(image_name)

        # Get a list of all the pixel values of current image
        pixel_values = UtilFunctions.get_pixel_values(curr_img)

        # Get average and standard deviation of pixel values
        mean, std = UtilFunctions.get_mean_std(pixel_values)

        # Calculate and print SNR of current image
        snr = mean / std

        sizes, perimeters = measure_size_and_perimeter(curr_img)
        # TODO DOES NOT WORK ATM
        sizes = UtilFunctions.print_largest_measurements(sizes[0], perimeters[0])

        snr_values_no_filter.append(snr)
        size_values_no_filter.append(np.sum(sizes))

    print('no filter, size : ', size_values_no_filter)
    print('no filter, snr : ', snr_values_no_filter)

    # Now, all the mean and std values are known for images (rect)1-4 that are used for the following:
    # Plot the graph of the relative discretization error of the size
    #plot_relative_discretization_error(np.array(mean_size), np.array(std_size), 'size', 'no_noise')
    # Plot the graph of the relative discretization error of the perimeter
    #plot_relative_discretization_error(np.array(mean_perimeter), np.array(std_perimeter), 'perimeter', 'no_noise')

    # Initialize date and time
    date_time_str = UtilFunctions.generate_date_time_str()

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

    # For storage of sizes and snr values of image series
    size_values = size_values_no_filter
    snr_values = snr_values_no_filter

    for image_name in image_name_list:
        # Load current image
        curr_img = UtilFunctions.obtain_image(image_name)

        # Gaussian filter with sigma value 3 applied (best performing filter)
        curr_img = dip.Gauss(curr_img, 3)

        #UtilFunctions.show_image_in_dip_view(curr_img, sleep_sec)

        # Get a list of all the pixel values of current image
        pixel_values = UtilFunctions.get_pixel_values(curr_img)

        # Get average and standard deviation of pixel values
        mean, std = UtilFunctions.get_mean_std(pixel_values)

        # Calculate and print SNR of current image
        snr = mean / std

        sizes, perimeters = measure_size_and_perimeter(curr_img)

        sizes = UtilFunctions.print_largest_measurements(sizes[0], perimeters[0])

        snr_values.append(snr)
        size_values.append(np.sum(sizes))

    plot_snr_measurements(size_values, snr_values)
    '''