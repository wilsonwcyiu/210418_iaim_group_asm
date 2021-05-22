import diplib
import numpy as np
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
    selected_cell_image = diplib.Image((image_sizes_values[0], image_sizes_values[1]), 1)
    selected_cell_image.Fill(0)

    # Draw past position and current position of cell
    diplib.DrawBox(selected_cell_image, [1, 1], [x_1_value, y_1_value])
    diplib.DrawBox(selected_cell_image, [2, 2], [x_2_value, y_2_value])

    CommonUtil.save_image_to_default_project_folder(selected_cell_image, "asm4",
                                                    "track_" + series_name + "_" + cells_list[
                                                        i].cell_display_name + "_from_" + str(
                                                        sequence_number - 1) + "_to_" + str(sequence_number) + ".tif")


# Segment to retrieve brightest cells in image
def segment_brightest_cells_ver2(img):
    img = diplib.ContrastStretch(img, 97, 100);            #ImageUtil.show_image_in_dip_view(img)

    segm_img = ImageUtil.segment_image_white(img)

    return segm_img

    # file_name = image_file_name + '_segmented.tif'
    # CommonUtil.save_image_to_default_project_folder(segm_img, "asm4", file_name)
    #
    # labeled_img = diplib.Label(segm_img, boundaryCondition=["remove"])
    #
    # return labeled_img


# Save image that shows all initial center positions of selected cells
def save_image_initial_selection(sorted_measurements, image_name, dir_name: str = "asm4", proj_dir_path: str = None):
    # Create new empty image
    selected_cells_image = diplib.Image((image_size_list[0], image_size_list[1]), 1)
    selected_cells_image.Fill(0)

    for i in range(15):
        # Get coordinates of centers of current cell
        x_coord = sorted_measurements[i][2]
        y_coord = sorted_measurements[i][3]
        # Draw center of current cell
        diplib.DrawBox(selected_cells_image, [2, 2], [x_coord, y_coord])

    CommonUtil.save_image_to_default_project_folder(selected_cells_image, dir_name, image_name, proj_dir_path)


# Save image that shows all initial center positions of selected cells
def generate_initial_cell_img(cell_list: list, img_width: int, img_height: int):
    # Create new empty image
    selected_cells_image = diplib.Image((img_width, img_height), 1)
    selected_cells_image.Fill(0)

    for cell in cell_list:
        # Get coordinates of centers of current cell
        x_coord = cell.x_y_coord_tuple[0]
        y_coord = cell.x_y_coord_tuple[1]
        # Draw center of current cell
        diplib.DrawBox(selected_cells_image, [2, 2], [x_coord, y_coord])

    return selected_cells_image
    # CommonUtil.save_image_to_default_project_folder(selected_cells_image, dir_name, image_name, proj_dir_path)




def create_new_empty_images_for_selected_cells(img_width: int, img_height: int, num_of_img_to_create: int):
    image_list = []
    # img_width: int = image_width_length_tuple[0]
    # img_height: int = image_width_length_tuple[1]
    elements_size: int = 2

    for _ in range(num_of_img_to_create):
        new_image: diplib.Image = diplib.Image((img_width, img_height), elements_size)      #  ImageUtil.show_image_in_dip_view(new_image)
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


    number_of_cells_to_trace: int = 15



    image_series_name: str = "MTLn3+EGF"    #'MTLn3-ctrl'
    image_series_name_list: list = [] #, 'MTLn3-ctrl']
    for idx in range(0, 30):
        image_suffix: str = CommonUtil.format_int_to_str_length(idx, to_length=4)
        image_series_name_list.append(image_series_name + image_suffix)



    first_img_name: str = image_series_name_list[0]
    first_image: diplib.Image = ImageUtil.obtain_diplib_image(first_img_name, input_dir)

    img_width, img_height = ImageUtil.obtain_image_width_height(first_image)

    segm_img: diplib.Image = segment_brightest_cells_ver2(first_image);         # Segment to get only brightest cells in foreground
    file_name: str = first_img_name + '_segmented.tif'
    CommonUtil.save_image_to_default_project_folder(segm_img, dir_name, file_name, project_dir=proj_dir_path)

    labeled_img: diplib.Image = diplib.Label(segm_img, boundaryCondition=["remove"]);              #ImageUtil.show_image_in_dip_view(labeled_img)

    measurement_list: np.ndarray = np.array(diplib.MeasurementTool.Measure(labeled_img, first_image, ['Size', 'Perimeter', 'Center']))      # Measure size and centers of cells
    sorted_measurement_list: np.flipud = np.flipud(measurement_list[np.argsort(measurement_list[:, 0])])        # Sort array based on size of cells (descending)




    selected_cell_list: list = []
    for i in range(number_of_cells_to_trace):
        size = sorted_measurement_list[i][0]
        perimeter = sorted_measurement_list[i][1]
        x_coord = sorted_measurement_list[i][2]
        y_coord = sorted_measurement_list[i][3]

        cell_display_name = "cell_" + str(i)
        current_cell = Cell(i, cell_display_name, x_y_coord_tuple=(x_coord, y_coord), perimeter=perimeter, area=size)
        selected_cell_list.append(current_cell)

    init_cell_img: diplib.Image = generate_initial_cell_img(selected_cell_list, img_width, img_height)
    image_name = first_img_name + '_initial_selection.tif'
    CommonUtil.save_image_to_default_project_folder(init_cell_img, dir_name, image_name, proj_dir_path)



    num_of_img_to_create = len(selected_cell_list)
    images_movement_trajectories_list: list = create_new_empty_images_for_selected_cells(img_width, img_height, num_of_img_to_create)  #:list(diplib.Image)
    for i in range(len(selected_cell_list)):
        cell = selected_cell_list[i]
        out_img: diplib.Image = images_movement_trajectories_list[i];      start_pixel_dimension: list = [4, 4]
        diplib.DrawBox(out_img, start_pixel_dimension, list(cell.x_y_coord_tuple))



    for idx in range(1, 30):
        image_file_name: str = image_series_name_list[idx]

        curr_img: diplib.Image = ImageUtil.obtain_diplib_image(image_file_name, input_dir)

        # Segment to get only brightest cells in foreground
        segm_img: diplib.Image = segment_brightest_cells_ver2(curr_img);            #ImageUtil.show_image_in_dip_view(segm_img)
        file_name = image_file_name + '_segmented.tif'
        CommonUtil.save_image_to_default_project_folder(segm_img, dir_name, file_name, project_dir=proj_dir_path)

        labeled_img = diplib.Label(segm_img, boundaryCondition=["remove"]);              #ImageUtil.show_image_in_dip_view(labeled_img)

        measurement_list: np.ndarray = np.array(diplib.MeasurementTool.Measure(labeled_img, curr_img, ['Size', 'Perimeter', 'Center']))     # Measure size and centers of cells
        sorted_measurement_list: np.flipud = np.flipud(measurement_list[np.argsort(measurement_list[:, 0])])        # Sort array based on size of cells (descending)

        for i in range(len(selected_cell_list)):
            selected_cell = selected_cell_list[i]

            # print(selected_cells[i].cell_display_name, ", ", selected_cells[i].area, ", ", selected_cells[i].perimeter, ", ", selected_cells[i].cell_xy_coord_tuple)

            # Past position
            x_1 = selected_cell.x_y_coord_tuple[0]
            y_1 = selected_cell.x_y_coord_tuple[1]

            # Save lowest euclidean distance
            lowest_eucl_dist = 9999999999   #img_width #image_size_list[0]
            # Save index of cell information with lowest euclidean distance
            index_lowest_dist = 0

            for j in range(len(sorted_measurement_list)):
                x_2 = sorted_measurement_list[j][2]
                y_2 = sorted_measurement_list[j][3]

                eucl_dist = math.sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)

                if eucl_dist < lowest_eucl_dist:
                    lowest_eucl_dist = eucl_dist
                    index_lowest_dist = j

            # print(sorted_measurements[index_lowest_dist])

            # Current position
            x_2 = sorted_measurement_list[index_lowest_dist][2]
            y_2 = sorted_measurement_list[index_lowest_dist][3]

            selected_cell.x_y_coord_tuple = (x_2, y_2)
            selected_cell.area = sorted_measurement_list[index_lowest_dist][0]
            selected_cell.perimeter = sorted_measurement_list[index_lowest_dist][1]

            diplib.DrawLine(images_movement_trajectories_list[i], [int(x_1), int(y_1)], [int(x_2), int(y_2)])

            # save_image_cell_movement_per_transition(image_sizes, x_1, y_1, x_2, y_2, image_series_name, selected_cells, sequence)

    save_movement_images_selected_cells_series(images_movement_trajectories_list, image_series_name, dir_name, proj_dir_path)






