from pprint import pprint

from all_asm.asm4.model.cell import Cell

if __name__ == '__main__':
    cell_list = []

    cell = Cell(2)
    cell.area = 1.1
    cell_list.append(cell)

    cell = Cell(1)
    cell.area = 1.2
    cell_list.append(cell)



    cell_list.sort(key=lambda x: x.cell_id, reverse=True)

    for cell in cell_list:
        print(cell)