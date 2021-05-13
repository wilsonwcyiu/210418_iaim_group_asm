import numpy as np
import diplib as dip
from diplib import PyDIPjavaio
import math

from numpy.core.multiarray import ndarray

from util.common_util import CommonUtil
from util.image_util import ImageUtil
from util.plot_util import PlotUtil
from all_asm.asm4.model.cell import Cell


# Save images that display past and current center position of every selected cell
def save_image_cell_movement_per_transition(image_sizes_values, x_1_value, y_1_value, x_2_value, y_2_value, series_name, cells_list, sequence_number):
    # Create new empty image
    selected_cell_image = dip.Image((image_sizes_values[0], image_sizes_values[1]), 1)
    selected_cell_image.Fill(0)

    # Draw past position and current position of cell
    dip.DrawBox(selected_cell_image, [1, 1], [x_1_value, y_1_value])
    dip.DrawBox(selected_cell_image, [2, 2], [x_2_value, y_2_value])

    CommonUtil.save_image_to_default_project_folder(selected_cell_image, "asm4",
                                                    "track_" + series_name + "_" + cells_list[
                                                        i].cell_display_name + "_from_" + str(
                                                        sequence_number - 1) + "_to_" + str(sequence_number) + ".tif")


# Segment to retrieve brightest cells in image
def segment_brightest_cells(img, image_file_name):
    img = dip.ContrastStretch(img, 97, 100);            #ImageUtil.show_image_in_dip_view(img)

    # print(img.Sizes())

    segm_img = ImageUtil.segment_image_white(img)

    print(segm_img.Sizes())

    file_name = image_file_name + '_segmented.tif'
    CommonUtil.save_image_to_default_project_folder(segm_img, "asm4", file_name)

    labeled_img = dip.Label(segm_img, boundaryCondition=["remove"])

    return labeled_img


# Save image that shows all initial center positions of selected cells
def save_image_initial_selection(sorted_measurements, image_name, dir_name: str = "asm4", proj_dir_path: str = None):
    # Create new empty image
    selected_cells_image = dip.Image((image_size_list[0], image_size_list[1]), 1)
    selected_cells_image.Fill(0)

    for i in range(15):
        # Get coordinates of centers of current cell
        x_coord = sorted_measurements[i][2]
        y_coord = sorted_measurements[i][3]
        # Draw center of current cell
        dip.DrawBox(selected_cells_image, [2, 2], [x_coord, y_coord])

    CommonUtil.save_image_to_default_project_folder(selected_cells_image, dir_name, image_name, proj_dir_path)


def create_new_empty_images_for_selected_cells(image_sizes_values: list):
    image_list = []
    img_width: int = image_sizes_values[0]
    img_height: int = image_sizes_values[1]
    elements_size: int = 2

    for _ in range(15):
        new_image: dip.Image = dip.Image((img_width, img_height), elements_size)      #  ImageUtil.show_image_in_dip_view(new_image)
        new_image.Fill(0)
        image_list.append(new_image)

    return image_list


def save_movement_images_selected_cells_series(image_series, series_name, dir_name: str = "asm4", proj_dir_path: str = None):
    for i in range(15):
        CommonUtil.save_image_to_default_project_folder(image_series[i], dir_name, "track_" + series_name + "_cell" + str(i) + ".tif", proj_dir_path)


if __name__ == '__main__':
    # first_image = ImageUtil.obtain_image('AxioCamIm01', CommonUtil.obtain_project_default_input_dir_path() + 'asm3/')
    # ImageUtil.show_image_in_dip_view(first_image)
    #
    # first_image = ImageUtil.obtain_image("MTLn3+EGF0000", CommonUtil.obtain_project_default_input_dir_path() + 'asm4/')
    # ImageUtil.show_image_in_dip_view(first_image)
    # CommonUtil.press_enter_to_continue()


    input_dir: str = CommonUtil.obtain_project_default_input_dir_path() + 'asm4/'
    proj_dir_path: str = CommonUtil.obtain_project_default_output_dir_path()
    dir_name: str = CommonUtil.generate_date_time_str()

    image_series_name_list: list = ['MTLn3+EGF'] #, 'MTLn3-ctrl']

    for image_series_name in image_series_name_list:
        first_image: dip.Image = ImageUtil.obtain_image(image_series_name + '0000', input_dir)

        image_size_list: list = first_image.Sizes()
        images_movement_trajectories_list: list = create_new_empty_images_for_selected_cells(image_size_list)  #:list(list)


        selected_cell_list: list = []
        for idx in range(30):
            image_file_name: str = image_series_name + str(idx).zfill(4)
            curr_img: dip.Image = ImageUtil.obtain_image(image_file_name, input_dir)

            # Segment to get only brightest cells in foreground
            labeled_img: dip.Image = segment_brightest_cells(curr_img, image_file_name);            ImageUtil.show_image_in_dip_view(labeled_img)

            # Measure size and centers of cells
            measurement_list: np.ndarray = np.array(dip.MeasurementTool.Measure(labeled_img, curr_img, ['Size', 'Perimeter', 'Center']))

            # for measurement in measurement_list:
            #     size = measurement[0];      perimeter = measurement[1];     x = measurement[2];         y = measurement[3]
            #     print(size, "\t", perimeter, "\t", x, "\t", y)
            # CommonUtil.press_enter_to_continue()

            # Sort array based on size of cells (descending)
            sorted_measurements: np.flipud = np.flipud(measurement_list[np.argsort(measurement_list[:, 0])])


            is_first_img: bool = (idx == 0)
            if is_first_img:
                save_image_initial_selection(sorted_measurements, image_file_name + '_initial_selection.tif', dir_name, proj_dir_path)

                for i in range(15):
                    size = sorted_measurements[i][0];       perimeter = sorted_measurements[i][1]
                    x_coord = sorted_measurements[i][2];    y_coord = sorted_measurements[i][3]

                    cell_display_name="cell_" + str(i)
                    current_cell = Cell(i, cell_display_name, cell_xy_coord_tuple = (x_coord, y_coord), perimeter = perimeter, area = size)
                    selected_cell_list.append(current_cell)

                    out_img: dip.Image = images_movement_trajectories_list[i];      start_pixel_dimension: list = [4, 4];       coord: list = [x_coord, y_coord]
                    dip.DrawBox(out_img, start_pixel_dimension, coord)


            # Consecutive images of the series
            elif not is_first_img:
                for i in range(len(selected_cell_list)):
                    selected_cell = selected_cell_list[i]

                    # print(selected_cells[i].cell_display_name, ", ", selected_cells[i].area, ", ", selected_cells[i].perimeter, ", ", selected_cells[i].cell_xy_coord_tuple)

                    # Past position
                    x_1 = selected_cell.cell_xy_coord_tuple[0]
                    y_1 = selected_cell.cell_xy_coord_tuple[1]

                    # Save lowest euclidean distance
                    lowest_eucl_dist = image_size_list[0]
                    # Save index of cell information with lowest euclidean distance
                    index_lowest_dist = 0

                    for j in range(len(sorted_measurements)):
                        x_2 = sorted_measurements[j][2]
                        y_2 = sorted_measurements[j][3]

                        eucl_dist = math.sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)

                        if eucl_dist < lowest_eucl_dist:
                            lowest_eucl_dist = eucl_dist
                            index_lowest_dist = j

                    # print(sorted_measurements[index_lowest_dist])

                    # Current position
                    x_2 = sorted_measurements[index_lowest_dist][2]
                    y_2 = sorted_measurements[index_lowest_dist][3]

                    selected_cell.cell_xy_coord_tuple = (x_2, y_2)
                    selected_cell.area = sorted_measurements[index_lowest_dist][0]
                    selected_cell.perimeter = sorted_measurements[index_lowest_dist][1]

                    dip.DrawLine(images_movement_trajectories_list[i], [int(x_1), int(y_1)], [int(x_2), int(y_2)])

                    # save_image_cell_movement_per_transition(image_sizes, x_1, y_1, x_2, y_2, image_series_name, selected_cells, sequence)

        save_movement_images_selected_cells_series(images_movement_trajectories_list, image_series_name, dir_name, proj_dir_path)






