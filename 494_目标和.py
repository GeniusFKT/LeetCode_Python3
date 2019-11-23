
# dynamic programming
# 1472ms/5.46%
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if S > 1000 or S < -1000:
            return 0

        array = [0 for _ in range(2001)]
        array[1000-nums[0]] += 1
        array[1000+nums[0]] += 1

        update_array = []

        for idx in range(1, len(nums)):
            update_array = [0 for _ in range(2001)]

            for j in range(len(update_array)):
                if j >= nums[idx]:
                    update_array[j] += array[j-nums[idx]]
                if j <= 2000 - nums[idx]:
                    update_array[j] += array[j+nums[idx]]

            array = update_array

        return array[1000 + S]

# avoid unnecessary loops
# 664ms/24.36%
class Solution1:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        sum_of_nums = sum(nums)

        if S > sum_of_nums or S < -sum_of_nums:
            return 0

        array = [0 for _ in range(2 * sum_of_nums + 1)]
        array[sum_of_nums-nums[0]] += 1
        array[sum_of_nums+nums[0]] += 1

        update_array = []

        for idx in range(1, len(nums)):
            update_array = [0 for _ in range(2 * sum_of_nums + 1)]

            for j in range(2 * sum_of_nums + 1):
                if j >= nums[idx]:
                    update_array[j] += array[j-nums[idx]]
                if j <= 2 * sum_of_nums - nums[idx]:
                    update_array[j] += array[j+nums[idx]]

            array = update_array

        return array[sum_of_nums + S]