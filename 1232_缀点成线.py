
# 68ms/98.16%
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        leng = len(coordinates)
        if leng == 2:
            return True
        if coordinates[0][0] == coordinates[1][0]:
            for idx in range(2, leng):
                if coordinates[idx][0] != coordinates[0][0]:
                    return False
            return True
        k = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        b = (coordinates[1][0] * coordinates[0][1] - coordinates[0][0] * coordinates[1][1]) / (coordinates[1][0] - coordinates[0][0])
        for idx in range(2, leng):
            if k * coordinates[idx][0] + b != coordinates[idx][1]:
                return False
        return True

# 72ms/94.66%
class Solution1:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        delta_x = coordinates[1][0] - coordinates[0][0]
        delta_y = coordinates[1][1] - coordinates[0][1]

        for idx in range(2, len(coordinates)):
            if (coordinates[idx][0] - coordinates[0][0]) * delta_y != (coordinates[idx][1] - coordinates[0][1]) * delta_x:
                return False

        return True