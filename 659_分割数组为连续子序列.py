class Solution:
    def isPossible(self, nums) -> bool:
        print("nums:", nums)
        result = False

        if len(nums) == 0:
            return True

        if len(nums) < 3:
            return False

        if self.isIncrease(nums):
            return True

        for i in range(len(nums) - 3):
            nums1 = self.findLeastElement(nums, i + 3)
            print("nums1:", nums1)
            print("nums2:", nums)
            if len(nums1) != 0:
                result = result or self.isPossible(nums1)
        return result

    def findLeastElement(self, nums, n):
        q = nums
        m = min(q)
        for i in range(n):
            if (m + i) in q:
                q.remove(m + i)
            else:
                return []
        return q

    def isIncrease(self, nums):
        for i in range(len(nums) - 1):
            if nums[i+1] - nums[i] != 1:
                return False
        return True

def main():
    nums = [1, 2, 3, 3, 4, 5]
    a = Solution()
    print(a.isPossible(nums))

main()