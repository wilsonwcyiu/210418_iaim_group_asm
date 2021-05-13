import numpy as np
import diplib as dip
from diplib import PyDIPjavaio
import math

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
    img = dip.ContrastStretch(img, 97, 100)

    print(img.Sizes())

    segm_img = ImageUtil.segment_image_white(img)

    print(segm_img.Sizes())

    file_name = image_file_name + '_segmented.tif'
    CommonUtil.save_image_to_default_project_folder(segm_img, "asm4", file_name)

    labeled_img = dip.Label(segm_img, boundaryCondition=["remove"])

    return labeled_img


# Save image that shows all initial center positions of selected cells
def save_image_initial_selection(sorted_measurements, image_name):
    # Create new empty image
    selected_cells_image = dip.Image((image_sizes[0], image_sizes[1]), 1)
    selected_cells_image.Fill(0)

    for i in range(15):
        # Get coordinates of centers of current cell
        x_coord = sorted_measurements[i][2]
        y_coord = sorted_measurements[i][3]
        # Draw center of current cell
        dip.DrawBox(selected_cells_image, [2, 2], [x_coord, y_coord])

    CommonUtil.save_image_to_default_project_folder(selected_cells_image, "asm4", image_name)


def create_new_empty_images_for_selected_cells(image_sizes_values):
    image_list = []

    for _ in range(15):
        new_image = dip.Image((image_sizes_values[0], image_sizes_values[1]), 1)
        new_image.Fill(0)
        image_list.append(new_image)

    return image_list


def save_movement_images_selected_cells_series(image_series, series_name):
    for i in range(15):
        CommonUtil.save_image_to_default_project_folder(image_series[i], "asm4", "track_" + series_name + "_cell" + str(i) + ".tif")


if __name__ == '__main__':
    first_image = ImageUtil.obtain_image('AxioCamIm01', CommonUtil.obtain_project_default_input_dir_path() + 'asm3/')
    ImageUtil.show_image_in_dip_view(first_image)

    first_image = ImageUtil.obtain_image("MTLn3+EGF0000", CommonUtil.obtain_project_default_input_dir_path() + 'asm4/')
    ImageUtil.show_image_in_dip_view(first_image)


    CommonUtil.press_enter_to_continue()


    input_dir: str = CommonUtil.obtain_project_default_input_dir_path() + 'asm4/'

    image_series_names = ['MTLn3+EGF', 'MTLn3-ctrl']

    for image_series_name in image_series_names:
        first_image = ImageUtil.obtain_image('AxioCamIm01', CommonUtil.obtain_project_default_input_dir_path() + 'asm3/')
        first_image = ImageUtil.obtain_image(image_series_name + '0000', input_dir)
        image_sizes = first_image.Sizes()

        selected_cells = []

        images_movement_trajectories_list = create_new_empty_images_for_selected_cells(image_sizes)

        for sequence in range(30):
            image_file_name = image_series_name + str(sequence).zfill(4)
            curr_img = ImageUtil.obtain_image(image_file_name + '.png', input_dir)

            # Segment to get only brightest cells in foreground
            labeled_img = segment_brightest_cells(curr_img, image_file_name)

            # Measure size and centers of cells
            measurements = np.array(dip.MeasurementTool.Measure(labeled_img, curr_img, ['Size', 'Perimeter', 'Center']))
            # Sort array based on size of cells (descending)
            sorted_measurements = np.flipud(measurements[np.argsort(measurements[:, 0])])

            # First image of the series
            if sequence == 0:
                save_image_initial_selection(sorted_measurements, image_file_name + '_initial_selection.tif')

                for i in range(15):
                    size = sorted_measurements[i][0]
                    perimeter = sorted_measurements[i][1]

                    x_coord = sorted_measurements[i][2]
                    y_coord = sorted_measurements[i][3]

                    current_cell = Cell(i)
                    current_cell.cell_display_name = "cell" + str(i)
                    current_cell.cell_xy_coord_tuple = (x_coord, y_coord)
                    current_cell.perimeter = perimeter
                    current_cell.area = size

                    selected_cells.append(current_cell)

                    # Draw square for starting position of current selected cell
                    dip.DrawBox(images_movement_trajectories_list[i], [4, 4], [x_coord, y_coord])

            # Consecutive images of the series
            else:
                for i in range(len(selected_cells)):
                    # print(selected_cells[i].cell_display_name, ", ", selected_cells[i].area, ", ", selected_cells[i].perimeter, ", ", selected_cells[i].cell_xy_coord_tuple)

                    # Past position
                    x_1 = selected_cells[i].cell_xy_coord_tuple[0]
                    y_1 = selected_cells[i].cell_xy_coord_tuple[1]

                    # Save lowest euclidean distance
                    lowest_eucl_dist = image_sizes[0]
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

                    selected_cells[i].cell_xy_coord_tuple = (x_2, y_2)
                    selected_cells[i].area = sorted_measurements[index_lowest_dist][0]
                    selected_cells[i].perimeter = sorted_measurements[index_lowest_dist][1]

                    dip.DrawLine(images_movement_trajectories_list[i], [int(x_1), int(y_1)], [int(x_2), int(y_2)])

                    # save_image_cell_movement_per_transition(image_sizes, x_1, y_1, x_2, y_2, image_series_name, selected_cells, sequence)

        save_movement_images_selected_cells_series(images_movement_trajectories_list, image_series_name)






