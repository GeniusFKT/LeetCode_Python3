import math

# 424ms/39.31%

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        ans = nums[0]
        for i in nums:
            ans = math.gcd(ans, i)

        return ans == 1