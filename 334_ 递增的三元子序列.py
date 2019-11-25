
# 56ms/100%
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if nums == []:
            return False
        t = max(nums) + 1
        one = two = t

        for num in nums:
            if num <= one:
                one = num
            elif num <= two:
                two = num
            else:
                return True

        return False
