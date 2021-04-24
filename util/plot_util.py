import os
from os import path

from matplotlib import pyplot


class PlotUtil():

    @staticmethod
    def save_plot_to_project_folder(plt: pyplot, dir_name: str, file_name: str):
        project_dir: str = "../../image_output/"
        dir_path_str: str = os.path.join(project_dir, dir_name)
        full_file_path: str = os.path.join(dir_path_str, file_name)

        if dir_name is not None and not path.exists(dir_path_str):
            os.mkdir(dir_path_str, 0x0755)

        plt.savefig(full_file_path)



    @staticmethod       # xy_tuple_list = [(0,0), (3,5), (5,5)]
    def create_plot(plot_id: int, plot_title: str, x_label: str, y_label: str, xy_tuple_list: list):
        pyplot.figure(plot_id)
        pyplot.clf()
        pyplot.title(plot_title)
        pyplot.xlabel(x_label)
        pyplot.ylabel(y_label)

        x_list = []
        y_list = []
        for xy_tuple in xy_tuple_list:
            x_list.append(xy_tuple[0])
            y_list.append(xy_tuple[1])

        pyplot.plot(x_list, y_list)

        return pyplot





    @staticmethod
    def plot_value_mean_stddev(plot_id: int, value_plot_title: str, x_label: str, y_label: str, value_list, mean_list, stddev_list):
        pyplot.figure(plot_id)
        pyplot.close()
        # plt.cla()
        # plt.clf()
        # plt.cla()

        fig, axs = plt.subplots(2)

        value_axs = axs[0]
        value_axs.set(xlabel=x_label, ylabel=y_label)
        value_axs.set_title(value_plot_title)
        value_axs.plot(value_list)

        mean_stddev_axs = axs[1]
        mean_stddev_axs.set(xlabel=x_label, ylabel=y_label)
        mean_stddev_axs.set_title("Mean and Standard Deviation")
        mean_stddev_axs.plot(mean_list, label='Mean')
        mean_stddev_axs.plot(stddev_list, label='Standard deviation')
        mean_stddev_axs.legend()

        # fig.tight_layout()

        # plt.pause(0.001)

        return pyplot



    @staticmethod
    def plot_multi_list(plot_id: int, plot_title: str, x_label: str, y_label: str, label_data_list_dict: dict):
        pyplot.figure(plot_id)
        pyplot.clf()

        pyplot.title(plot_title)
        pyplot.xlabel(x_label)
        pyplot.ylabel(y_label)

        for key, item in label_data_list_dict.items():
            pyplot.plot(item, label=key)

        pyplot.legend()

        # plt.pause(0.001)

        return pyplot


    @staticmethod
    def plot(plot_id: int, plot_title: str, x_label: str, y_label: str, data_list: list):
        pyplot.figure(plot_id)
        pyplot.clf()
        pyplot.title(plot_title)
        pyplot.xlabel(x_label)
        pyplot.ylabel(y_label)

        pyplot.plot(data_list)

        # plt.pause(0.001)

        return pyplot
