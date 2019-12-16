
# 56ms/93.14
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                if fast != slow:
                    nums[slow] = nums[fast]
                slow += 1

        for fast in range(slow, len(nums)):
            nums[fast] = 0