from typing import Tuple

class PositionConverter:
    
    @classmethod
    def convert(self, list_index: int, col_count: int) -> Tuple[int, int]:
        row = list_index / col_count
        col = list_index % col_count
        
        return row, col
        