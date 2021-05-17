import numpy as np
import diplib
import math
import matplotlib.pyplot as plt

from util.common_util import CommonUtil
from util.image_util import ImageUtil
from util.plot_util import PlotUtil
from all_asm.asm4.model.cell import Cell


# Create table showing initial shape and texture features of cells from image series
def create_table_shape_texture_features(cell_list: list, image_series_name: str):
    line: str = '-' * 105

    print("\n\nShape and texture feature table of image series ", image_series_name)
    print(line)
    print('{:^10s}{:^10s}{:^10s}{:^15s}{:^10s}{:^20s}{:^15s}{:^15s}'.format("cell id", "area", "perimeter", "roundness",
                                                                            "mean", "standard deviation", "smoothness",
                                                                            "uniformity"))
    print(line)
    for cell in cell_list:
        print(
            '{:^10s}{:^10.0f}{:^10.2f}{:^15.2f}{:^10.2f}{:^20.2f}{:^15.2f}{:^15.2f}'.format(
                str(cell.cell_id), float(cell.area_list[0]), float(cell.perimeter_list[0]),
                float(cell.roundness_list[0]), float(cell.mean_list[0]),
                float(cell.std_list[0]), float(cell.smoothness_list[0]),
                float(cell.uniformity_list[0]))
        )


def create_total_distance_trajectory(trajectory_list: list):
    # Total distance value saved
    total_dist: float = 0
    # Saves total distance per minute
    distance_data: list = [total_dist]

    # Go through movement trajectory
    for step in range(1, len(trajectory_list)):
        coord_tuple_prev: tuple = trajectory_list[step - 1]
        coord_tuple_curr: tuple = trajectory_list[step]

        # Calculate euclidean distance between previous and current position
        eucl_dist: float = math.sqrt(
            (coord_tuple_curr[0] - coord_tuple_prev[0]) ** 2 + (coord_tuple_curr[1] - coord_tuple_prev[1]) ** 2)

        # Add to previous distance
        total_dist += eucl_dist

        distance_data.append(total_dist)

    return distance_data


# Create table showing velocity and distance of cells from image series
def create_table_velocity_distance(cell_list: list, image_series_name: str):
    line: str = '-' * 110

    print("\n\nVelocity and total distance table of image series ", image_series_name)
    print(line)
    print('{:^10s}{:^30s}{:^30s}{:^40s}'.format("cell id", "velocity (in pixels/min)", "distance (in pixels)",
                                                "tracked movement transitions"))
    print(line)

    for cell in cell_list:
        trajectory_list: list = cell.cell_trajectory_data_tuple_list

        distance_data: list = create_total_distance_trajectory(trajectory_list)

        total_dist: float = distance_data[-1]
        velocity: float = total_dist / len(distance_data)

        print(
            '{:^10s}{:^30.2f}{:^30.2f}{:^40.0f}'.format(
                str(cell.cell_id), float(velocity), float(total_dist), float(len(distance_data)))
        )


# Create a plot that shows the distance over time for every cell
def create_graph_distance_over_time(cell_list: list, image_series_name: str):
    # x-axis: time in minutes
    x_axis = np.linspace(0, 29, 30)

    ax = plt.axes()

    # Go through every cell in list
    for cell in cell_list:
        trajectory_list: list = cell.cell_trajectory_data_tuple_list

        # Get list with summed up distances
        distance_data: list = create_total_distance_trajectory(trajectory_list)

        data_total_number: int = len(distance_data)
        # Check if length complies with number of x-axis values
        if data_total_number != 30:
            difference: int = 30 - data_total_number

            for _ in range(difference):
                distance_data.append(None)

        ax.plot(x_axis, distance_data, label='cell ' + str(cell.cell_id))
        ax.set(xlabel='time in minutes', ylabel='distance in pixels',
               title='Plot of Distance over Time of Image Series ' + image_series_name)
        ax.legend()

    PlotUtil.save_plot_to_project_folder(plt, 'asm4', image_series_name + '_dist_over_time.png')
    plt.clf()


# Segmentation resulting in foreground consisting of brightest cells (depending on parameters upper and lowerbound) -> saved in image output file
def segm_for_brightest_cells(img: diplib.Image, image_file_name: str, proj_dir: str, lower_bound: int,
                             upper_bound: int):
    # Get brightest cells
    img: diplib.Image = diplib.ContrastStretch(img, lower_bound, upper_bound)
    # Get binary image
    segmented_img: diplib.Image = ImageUtil.segment_image_white(img)

    file_name_to_save: str = image_file_name + '_segm_brightest_cells'
    CommonUtil.save_image_to_default_project_folder_imageio(segmented_img, 'asm4', file_name_to_save, proj_dir)

    return segmented_img


# Create a list of empty images for every selected cell in image series
def create_empty_images_for_selected_cells(img_width: int, img_height: int, total_tracked_cells: int):
    image_list = []

    for _ in range(total_tracked_cells):
        new_img: diplib.Image = diplib.Image((img_width, img_height), 1)
        new_img.Fill(0)

        image_list.append(new_img)

    return image_list


# Generate and save image that shows centers of initially selected cells
def generate_and_save_initial_cell_selection_img(selected_cells: list, img_width: int, img_height: int, image_name: str,
                                                 proj_dir: str):
    # Create new empty image
    new_img = diplib.Image((img_width, img_height), 1)
    new_img.Fill(0)

    for cell in selected_cells:
        # Get coordinates of centers of current cell
        x_coord: float = cell.x_y_coord_tuple[0]
        y_coord: float = cell.x_y_coord_tuple[1]

        # Draw center of current cell
        diplib.DrawBox(new_img, [3, 3], [int(x_coord), int(y_coord)])

    CommonUtil.save_image_to_default_project_folder_imageio(new_img, 'asm4', image_name + '_initial_selection', proj_dir)


# Obtain the list of all image file names of every image series -> [[list of all images of series A][list of all images of series B]]
def obtain_image_file_names_in_series(image_series_list: list, image_total: int):
    all_series_file_names: list = []
    for image_series in image_series_list:
        all_file_names_per_series: list = []
        for i in range(0, image_total):
            image_suffix: str = CommonUtil.format_int_to_str_length(i, to_length=4)
            all_file_names_per_series.append(image_series + image_suffix)
        all_series_file_names.append(all_file_names_per_series)

    return all_series_file_names


# Convert labeled image to list of candidate cells
def convert_labeled_img_to_cell_list(labeled_img: diplib.Image, original_img: diplib.Image):
    # Generate list of measurements
    measurement_list: np.ndarray = np.array(diplib.MeasurementTool.Measure(labeled_img, original_img,
                                                                           ['Size', 'Perimeter', 'Center', 'Roundness',
                                                                            'Mean', 'StandardDeviation', 'MinVal',
                                                                            'MaxVal']))

    cell_list: list = []
    cell_id: int = 0

    for measurement in measurement_list:
        cell: Cell = Cell(cell_id)
        cell.cell_display_name = "cell_" + str(cell_id)

        # Location and shape features
        cell.area = measurement[0]
        cell.perimeter = measurement[1]
        cell.x_y_coord_tuple = (measurement[2], measurement[3])
        cell.roundness = measurement[4]
        cell.mean = measurement[5]
        cell.std = measurement[6]
        cell.min_val = measurement[7]
        cell.max_val = measurement[8]
        cell.smoothness = CommonUtil.calc_smoothness(cell.std)
        cell.uniformity = CommonUtil.calc_uniformity(cell.min_val, cell.max_val)

        cell_list.append(cell)

        cell_id += 1

    return cell_list


if __name__ == '__main__':
    # Initialize cell tracking parameters
    number_of_cells_to_trace: int = 15
    cell_size_variation_rate: float = 0.4
    cell_max_pixel_movement_distance: int = 110

    # Configure files and directories
    input_dir: str = CommonUtil.obtain_project_default_input_dir_path() + 'asm4/'
    proj_dir_path: str = '../../image_output/'
    image_series_name_list: list = ['MTLn3+EGF', 'MTLn3-ctrl']

    # Get list of images per series
    image_series_file_name_list = obtain_image_file_names_in_series(image_series_name_list, 30)

    total_amount_series: int = len(image_series_file_name_list)

    # Go through every image series
    for i in range(total_amount_series):
        all_images: list = image_series_file_name_list[i]

        # ---- Selection of cells that will be checked ----

        first_image_name: str = all_images[0]
        first_image: diplib.Image = ImageUtil.obtain_image_imageio(first_image_name + '.png', input_dir)

        img_width, img_height = ImageUtil.obtain_image_width_height(first_image)

        # Use this method of segmentation to ensure selection of brightest cells
        segm_img: diplib.Image = segm_for_brightest_cells(first_image, first_image_name, proj_dir_path, 80, 100)

        # Label the found brightest cells excluding the cells positioned at border of image
        labeled_img: diplib.Image = diplib.Label(segm_img, boundaryCondition=["remove"])

        # Get all candidate (bright) cells in a list with information
        all_candidate_cells_list: list = convert_labeled_img_to_cell_list(labeled_img, first_image)

        # Sort the list of candidate cells based on size
        all_candidate_cells_list.sort(key=lambda x: x.area, reverse=True)
        # Select the largest cells that will be tracked
        selected_cell_list: list = all_candidate_cells_list[0: number_of_cells_to_trace]

        # Generate and save image that shows the initial selection of cells to be tracked
        generate_and_save_initial_cell_selection_img(selected_cell_list, img_width, img_height,
                                                     image_series_name_list[i], proj_dir_path)

        # Generate empty images for every tracked cell to save its movement tracks
        images_movement_trajectory_list: list = create_empty_images_for_selected_cells(img_width, img_height,
                                                                                       number_of_cells_to_trace)

        # Save initial position and shape feature values of selected cells and draw this location in the images
        for j in range(0, len(selected_cell_list)):
            selected_cell = selected_cell_list[j]

            coord: tuple = selected_cell.x_y_coord_tuple
            perimeter: float = selected_cell.perimeter
            area: float = selected_cell.area
            roundness: float = selected_cell.roundness
            std: float = selected_cell.std
            mean: float = selected_cell.mean
            smoothness: float = selected_cell.smoothness
            uniformity: float = selected_cell.uniformity

            selected_cell.cell_trajectory_data_tuple_list.append(coord)
            selected_cell.perimeter_list.append(perimeter)
            selected_cell.area_list.append(area)
            selected_cell.roundness_list.append(roundness)
            selected_cell.std_list.append(std)
            selected_cell.mean_list.append(mean)
            selected_cell.smoothness_list.append(smoothness)
            selected_cell.uniformity_list.append(uniformity)

            diplib.DrawBox(images_movement_trajectory_list[j], [3, 3], list(coord))

        # ---- Track selected cells in next image series (0001 - 0029) ----
        for idx in range(1, 30):
            image_file_name: str = all_images[idx]

            curr_img: diplib.Image = ImageUtil.obtain_image_imageio(image_file_name + '.png', input_dir)

            # Segment to get cells in foreground
            segm_img: diplib.Image = segm_for_brightest_cells(curr_img, image_file_name, proj_dir_path, 80, 100)
            # Label cells
            labeled_img: diplib.Image = diplib.Label(segm_img)

            # Get cell information and save these cells in list
            all_candidate_cells_list: list = convert_labeled_img_to_cell_list(labeled_img, curr_img)

            # Run through tracked/selected cells
            for j in range(len(selected_cell_list)):
                selected_cell: Cell = selected_cell_list[j]

                # Check if still tracking
                if selected_cell.last_cell_states != "normal":
                    continue

                # Past position of current tracked/selected cell
                x_1: float = selected_cell.x_y_coord_tuple[0]
                y_1: float = selected_cell.x_y_coord_tuple[1]

                # Only collect cells that are within size change rate
                within_size_change_range_list: list = []

                for candidate_cell in all_candidate_cells_list:
                    size_change_rate: float = (candidate_cell.area - selected_cell.area) / selected_cell.area

                    if size_change_rate < cell_size_variation_rate:
                        within_size_change_range_list.append(candidate_cell)

                if len(within_size_change_range_list) == 0:
                    selected_cell.last_cell_states = "no cell is detected within max size variation range"
                    continue

                lowest_eucl_dist: float = 999999.9
                best_match_cell: Cell = None

                for within_size_change_range_cell in within_size_change_range_list:
                    x_2: float = within_size_change_range_cell.x_y_coord_tuple[0]
                    y_2: float = within_size_change_range_cell.x_y_coord_tuple[1]

                    eucl_dist = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)

                    if eucl_dist <= lowest_eucl_dist:
                        lowest_eucl_dist = eucl_dist
                        best_match_cell = within_size_change_range_cell

                if lowest_eucl_dist > cell_max_pixel_movement_distance:
                    selected_cell.last_cell_states = "no qualified cell is detected within max movement distance: " + str(
                        lowest_eucl_dist)
                    continue

                '''
                # Keep track of cells that are inside euclidean distance range of current tracked cell
                within_eucl_cell_list: list = []

                # Run through all cells in current image and select cells that are within acceptable range
                for candidate_cell in all_candidate_cells_list:
                    # Position of current cell
                    x_2: float = candidate_cell.x_y_coord_tuple[0]
                    y_2: float = candidate_cell.x_y_coord_tuple[1]

                    # Calculate euclidean distance
                    eucl_dist = math.sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)

                    # Check if distance is within maximum distance
                    if eucl_dist <= cell_max_pixel_movement_distance:
                        within_eucl_cell_list.append(candidate_cell)


                # Check if there are no cells within acceptable range
                if len(within_eucl_cell_list) == 0:
                    selected_cell.last_cell_states = "no cell is detected within max movement distance"
                    continue


                # Select cell with lowest size change with tracked cell
                lowest_size_change_rate: int = 9999999
                within_size_change_rate_cnt: int = 0
                best_match_cell: Cell = None

                for within_eucl_cell in within_eucl_cell_list:
                    # Calculate size change rate
                    size_change_rate: float = (within_eucl_cell.area - selected_cell.area) / selected_cell.area
                    # Checks if cell is not too different of size
                    is_within_size_change_rate: bool = (-cell_size_variation_rate <= size_change_rate <= cell_size_variation_rate)

                    if is_within_size_change_rate:
                        within_size_change_rate_cnt += 1
                        if size_change_rate < lowest_size_change_rate:
                            lowest_size_change_rate = size_change_rate
                            best_match_cell = within_eucl_cell


                # Save in cell information how much cells have been qualified to be same cell in this transition
                selected_cell.total_qualified_cell_count_list.append(within_size_change_rate_cnt)
                

                # Check if there are no cells within acceptable range of size change rate
                if within_size_change_rate_cnt == 0:
                    selected_cell.last_cell_states = "no detected cell is within max area change rate"
                    continue
                    
                '''

                # Current position best qualified cell
                x_2: float = best_match_cell.x_y_coord_tuple[0]
                y_2: float = best_match_cell.x_y_coord_tuple[1]

                # Override cell information of past cell status to current cell status
                selected_cell.x_y_coord_tuple = (x_2, y_2)
                selected_cell.area = best_match_cell.area
                selected_cell.perimeter = best_match_cell.perimeter
                selected_cell.roundness = best_match_cell.roundness
                selected_cell.std = best_match_cell.std
                selected_cell.mean = best_match_cell.mean
                selected_cell.smoothness = best_match_cell.smoothness
                # Add new values to list of past values of shape and movement features
                selected_cell.cell_trajectory_data_tuple_list.append((x_2, y_2))
                selected_cell.perimeter_list.append(best_match_cell.perimeter)
                selected_cell.area_list.append(best_match_cell.area)
                selected_cell.roundness_list.append(best_match_cell.roundness)
                selected_cell.std_list.append(best_match_cell.std)
                selected_cell.mean_list.append(best_match_cell.mean)
                selected_cell.smoothness_list.append(best_match_cell.smoothness)
                selected_cell.uniformity_list.append(best_match_cell.uniformity)

                # Draw movement line in image of tracked cell
                diplib.DrawLine(images_movement_trajectory_list[j], [int(x_1), int(y_1)], [int(x_2), int(y_2)])

        # Save images selected cells
        cell_id: int = 0

        for image in images_movement_trajectory_list:
            CommonUtil.save_image_to_default_project_folder_imageio(image, 'asm4',
                                                                    image_series_name_list[i] + '_tracking_cell_' +
                                                                    str(cell_id) + '.png', proj_dir_path)
            cell_id += 1

        # Print numerical information of tracked cells
        selected_cell_list.sort(key=lambda x: x.cell_id, reverse=False)
        print("\n\n--- Tracked cells of image series " + image_series_name_list[i] + "---\n\n")
        for selected_cell in selected_cell_list:
            print("cell_id: ", selected_cell.cell_id, "\t",
                  "last_step: ", str(len(selected_cell.cell_trajectory_data_tuple_list)), "\t",
                  "last_states: ", selected_cell.last_cell_states, "\n",
                  "trajectory_data", selected_cell.cell_trajectory_data_tuple_list, "\n",
                  "perimeter_data", selected_cell.perimeter_list, "\n",
                  "area_data", selected_cell.area_list, "\n",
                  "roundness_data", selected_cell.roundness_list, "\n",
                  "std_data", selected_cell.std_list, "\n",
                  "mean_data", selected_cell.mean_list, "\n",
                  "smoothness_data", selected_cell.smoothness_list, "\n",
                  "uniformity_data", selected_cell.uniformity_list, "\n",
                  "qualified_cell_cnt_in_each_image: ", selected_cell.total_qualified_cell_count_list, "\n"
                  )

        # Show results
        create_table_shape_texture_features(selected_cell_list, image_series_name_list[i])
        create_table_velocity_distance(selected_cell_list, image_series_name_list[i])
        create_graph_distance_over_time(selected_cell_list, image_series_name_list[i])
