
# 556ms/62.93%
# Binary Search
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        min_v = (sum(piles) - 1) // H + 1
        max_v = max(piles)

        while max_v > min_v + 1:
            v = (max_v + min_v) // 2
            if self.isPossible(piles, H, v):
                max_v = v
            else:
                min_v = v

        if self.isPossible(piles, H, min_v):
            return min_v
        else:
            return max_v

    def isPossible(self, piles, H, v):
        total_time = 0
        for i in piles:
            total_time += ((i - 1) // v) + 1
        if total_time > H:
            return False
        else:
            return True

