from util.common_util import CommonUtil


class Cell():


    def __init__(self, cell_id, cell_display_name = None, cell_xy_coord_tuple: tuple = None, perimeter: float = None, area: float = None):
        self.cell_id: int = cell_id
        self.cell_display_name: str = None

        self.cell_xy_coord_tuple: tuple = cell_xy_coord_tuple

        self.perimeter: float = perimeter
        self.area: float = area

        self.cell_trajectory_data_tuple_list: list = []
        self.similar_area_cell_data_dict: dict = {}



    def __str__(self):
        return '%s(%s)' % (
            type(self).__name__,', '.join('%s=%s' % item for item in vars(self).items())
        )
        # CommonUtil.auto_str(self)