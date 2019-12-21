
# 176ms/94.95%
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0

        total = sum(nums)
        partial = 0
        for idx in range(len(nums)):
            if idx > 0:
                partial += nums[idx - 1]
            if 2 * partial + nums[idx] == total:
                return idx

        return -1