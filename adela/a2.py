import diplib as dip
import numpy as np
import matplotlib.pyplot as plt


def measure_size_and_perimeter(image):
    rectangles = image < 65
    rectangles = dip.Label(rectangles)
    px_measure = dip.MeasurementTool.Measure(rectangles, image, ['Size', 'Perimeter'])
    print(px_measure)
    size = np.array(px_measure['Size']).transpose()
    perimeter = np.array(px_measure['Perimeter']).transpose()

    return size, perimeter


def mean_std(array):
    mean = np.mean(array)
    std = np.std(array)

    return mean, std


def plot_relative_discretization_error(mean_array, std_array, label):
    sqrt_mean = np.sqrt(mean_array)
    cv = std_array/mean_array

    fig, ax = plt.subplots()
    ax.plot(sqrt_mean, cv)
    ax.set(xlabel='square root of the mean',
           ylabel='coefficient of variation',
           title='The relative discretization error of '+label)
    fig.savefig(label)
    plt.show()

if __name__ == '__main__':
    image_names = ['rect1', 'rect2', 'rect3', 'rect4']

    mean_size = []
    std_size = []
    mean_perimeter = []
    std_perimeter = []
    # measuring area and perimeter of the rectangles in images (Part 2.1 task 1,2)
    for image in image_names:
        img = dip.ImageRead(image)
        img.Show()
        dip.Show(img)
        size, perimeter = measure_size_and_perimeter(img)

        mean, std = mean_std(size)
        print("Size mean:", mean, "std:", std)
        mean_size.append(mean)
        std_size.append(std)

        mean, std = mean_std(perimeter)
        print("Perimeter mean:", mean, "std:", std)
        mean_perimeter.append(mean)
        std_perimeter.append(std)

    # plot of the relative discretization error of the size (Part 2.2 task 3)
    plot_relative_discretization_error(np.array(mean_size), np.array(std_size), 'size')

    # plot of the relative discretization error of the perimeter (Part 2.2 task 4)
    plot_relative_discretization_error(np.array(mean_perimeter), np.array(std_perimeter), 'perimeter')




