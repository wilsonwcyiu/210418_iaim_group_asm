import numpy as np
import diplib as dip
from diplib import PyDIPjavaio
import math

from util.common_util import CommonUtil
from util.image_util import ImageUtil
from util.plot_util import PlotUtil
from all_asm.asm4.model.cell import Cell


def segment_brightest_cells(img, image_file_name):
    img = dip.ContrastStretch(img, 97, 100)

    segm_img = ImageUtil.segment_image_white(img)

    file_name = image_file_name + '_segmented.tif'
    CommonUtil.save_image_to_default_project_folder(segm_img, "asm4", file_name)

    labeled_img = dip.Label(segm_img, boundaryCondition=["remove"])

    return labeled_img


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


if __name__ == '__main__':
    input_dir: str = CommonUtil.obtain_project_default_input_dir_path() + 'asm4/'

    image_series_names = ['MTLn3+EGF', 'MTLn3-ctrl']

    for image_series_name in image_series_names:

        first_image = ImageUtil.obtain_image(image_series_name + '0000.png', input_dir)
        image_sizes = first_image.Sizes()

        selected_cells = []

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

            # Consecutive images of the series
            else:

                for i in range(len(selected_cells)):
                    #print(selected_cells[i].cell_display_name, ", ", selected_cells[i].area, ", ", selected_cells[i].perimeter, ", ", selected_cells[i].cell_xy_coord_tuple)

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

                    #print(sorted_measurements[index_lowest_dist])

                    # Current position
                    x_2 = sorted_measurements[index_lowest_dist][2]
                    y_2 = sorted_measurements[index_lowest_dist][3]

                    selected_cells[i].cell_xy_coord_tuple = (x_2, y_2)
                    selected_cells[i].area = sorted_measurements[index_lowest_dist][0]
                    selected_cells[i].perimeter = sorted_measurements[index_lowest_dist][1]

                    # Create new empty image
                    selected_cell_image = dip.Image((image_sizes[0], image_sizes[1]), 1)
                    selected_cell_image.Fill(0)

                    # Draw past position and current position of cell
                    dip.DrawBox(selected_cell_image, [1, 1], [x_1, y_1])
                    dip.DrawBox(selected_cell_image, [2, 2], [x_2, y_2])

                    CommonUtil.save_image_to_default_project_folder(selected_cell_image, "asm4", "track_" + image_series_name + "_" + selected_cells[i].cell_display_name + "_from_" + str(sequence-1) + "_to_" + str(sequence) + ".tif")






