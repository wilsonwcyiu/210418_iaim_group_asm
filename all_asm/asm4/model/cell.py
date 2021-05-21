from util.common_util import CommonUtil
import diplib


class Cell():


    def __init__(self, cell_id, cell_display_name = None, x_y_coord_tuple: tuple = None, perimeter: float = None, area: float = None, roundness: float = None, std: float = None, mean: float = None, smoothness: float = None, uniformity: float = None):
        self.cell_id: int = cell_id
        self.cell_display_name: str = None

        self.cell_track_img: diplib.Image = None

        self.x_y_coord_tuple: tuple = x_y_coord_tuple

        self.perimeter: float = perimeter
        self.area: float = area
        self.roundness: float = roundness
        self.std: float = std
        self.mean: float = mean
        self.smoothness: float = smoothness
        self.uniformity: float = uniformity
        self.min_val = None
        self.max_val = None

        # report data
        self.cell_trajectory_data_tuple_list: list = []
        self.total_qualified_cell_count_list: list = []
        self.perimeter_list: list = []
        self.area_list: list = []
        self.roundness_list: list = []
        self.std_list: list = []
        self.mean_list: list = []
        self.smoothness_list: list = []
        self.uniformity_list: list = []
        self.last_cell_states: str = "normal"


    def __str__(self):
        return '%s(%s)' % (
            type(self).__name__,', '.join('%s=%s' % item for item in vars(self).items())
        )
        # CommonUtil.auto_str(self)