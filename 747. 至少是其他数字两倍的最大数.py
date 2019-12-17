
# 32ms/99.36
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        fir = -1
        sec = -1
        idx = -1
        if len(nums) == 1:
            return 0

        for i in range(len(nums)):
            if nums[i] > fir:                
                sec = fir
                fir = nums[i]
                idx = i

            elif nums[i] > sec:
                sec = nums[i]

        if fir >= 2 * sec:
            return idx
        else:
            return -1
