
# 424ms/68.35%
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        count = {}
        for num in nums:
            if count.get(num) is None:
                count[num] = 1
            else:
                count[num] += 1

        ans = 0
        count = sorted(count.items())
        for idx in range(len(count) - 1):
            if count[idx+1][0] - count[idx][0] == 1:
                if count[idx+1][1] + count[idx][1] > ans:
                    ans = count[idx+1][1] + count[idx][1]

        return ans


# 408ms/75.54%
class Solution1:
    def findLHS(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if count.get(num) is None:
                count[num] = 1
            else:
                count[num] += 1

        ans = 0
        for key in count.keys():
            if count.get(key + 1) is not None:
                if count[key+1] + count[key] > ans:
                    ans = count[key+1] + count[key]                

        return ans