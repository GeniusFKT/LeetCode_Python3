
# 288ms/85.89%
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        start, end, count = {}, {}, {}
        # iterate the list
        for idx in range(len(nums)):
            if start.get(nums[idx]) is None:
                start[nums[idx]] = idx
            end[nums[idx]] = idx
            if count.get(nums[idx]) is None:
                count[nums[idx]] = 1
            else:
                count[nums[idx]] += 1

        # count the minimum interval
        maximum = max(count.values())
        ans = len(nums)
        for i in count.keys():
            if count[i] == maximum:
                if end[i] - start[i] + 1 < ans:
                    ans = end[i] - start[i] + 1
        return ans