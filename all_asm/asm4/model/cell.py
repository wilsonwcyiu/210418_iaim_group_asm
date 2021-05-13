class Cell():


    def __init__(self, cell_id, cell_display_name = None, cell_xy_coord_tuple: tuple = None, perimeter: float = None, area: float = None):
        self.cell_id: int = cell_id
        self.cell_display_name: str = None

        self.cell_xy_coord_tuple: tuple = cell_xy_coord_tuple

        self.perimeter: float = perimeter
        self.area: float = area