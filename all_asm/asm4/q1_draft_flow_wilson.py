from all_asm.asm4.model.cell import Cell

if __name__ == '__main__':
    print("start")

    # system config
    max_cell_movement_distance_per_frame: int = 10



    cell_id_dict: dict = {}

    # dummy data
    cell1: Cell = Cell(1, cell_display_name="cell_1_dummy");    cell2: Cell = Cell(2, cell_display_name="cell_2_dummy")
    cell_id_dict[cell1.cell_id] = cell1;    cell_id_dict[cell2.cell_id] = cell2
    image_cell_dict_list: list = [cell_id_dict]
    #=== end dummy data

    total_images = 30
    for img_idx in range(0, total_images - 1):
        last_img_cell_dict: dict = image_cell_dict_list[img_idx]
        next_img_cell_dict: dict = {}
        for cell_id, cell in last_img_cell_dict.items():
            print(cell_id)
            print(cell.cell_xy_coord_tuple)
            print(cell.area)
            print(cell.perimeter)
            # find next cell info

        image_cell_dict_list.append(next_img_cell_dict)




print("end")
