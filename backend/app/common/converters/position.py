from typing import Tuple

class PositionConverter:
    
    @classmethod
    def to_cell_position(self, list_index: int, col_count: int) -> Tuple[int, int]:
        if col_count == 0:
            return 0, 0
        
        row = list_index // col_count
        col = list_index % col_count
        
        return row, col
        