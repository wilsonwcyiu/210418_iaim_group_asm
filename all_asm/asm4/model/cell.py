class Cell():


    def __init__(self, cell_id, cell_display_name = None):
        self.cell_id: int = cell_id
        self.cell_display_name: str = None

        self.cell_xy_coord_tuple: tuple = None

        self.perimeter: float = None
        self.area: float = None