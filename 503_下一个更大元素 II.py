
# 232ms/91.69%
# 单调栈
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        s = []
        ans = [-1 for _ in range(len(nums))]

        for index in range(2 * len(nums)):
            idx = index % len(nums)
            if len(s) == 0:
                s.append([idx, nums[idx]])
            else:
                while len(s) != 0:
                    if s[-1][1] >= nums[idx]:
                        s.append([idx, nums[idx]])
                        break
                    else:
                        ele = s.pop()
                        ans[ele[0]] = nums[idx]
                s.append([idx, nums[idx]])

        return ans


            