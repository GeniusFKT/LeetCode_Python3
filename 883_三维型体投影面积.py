import numpy as np

# numpy solution with less efficiency
# 188ms
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        grid = np.array(grid)
        return np.sum(np.max(grid, axis=0)) + np.sum(np.max(grid, axis=1)) + np.nonzero(grid)[0].shape[0]

# 96ms
class Solution1:
    def projectionArea(self, grid: List[List[int]]) -> int:
        area = 0
        col_max = [0 for _ in range(len(grid[0]))]
        for row in grid:
            row_max = 0
            for idx in range(len(row)):
                if row[idx] > row_max:
                    row_max = row[idx]
                if row[idx] > col_max[idx]:
                    col_max[idx] = row[idx]
                if row[idx] != 0:
                    area += 1
            area += row_max
        area += sum(col_max)

        return area

