import matplotlib.pyplot as plt
import numpy as np


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
    print("starting...")

    mean_array = [1,2,3,4,5]
    std_array = [5,4,3,2,1]
    label = "label"

    a = np.array(mean_array)
    print(type(a))
    plot_relative_discretization_error(mean_array, std_array, label)
