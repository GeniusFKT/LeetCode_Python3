
# 60ms/98.94%
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)

        # basic situation
        if length <= 1:
            return length

        write_ptr = 1
        read_ptr = 2

        # the number in read_ptr may be equal to which in write_ptr or not
        # as long as it's different from write_ptr - 1
        # then it's a valid value and should be written into the array
        for read_ptr in range(2, length):
            if nums[read_ptr] != nums[write_ptr - 1]:
                write_ptr += 1
                nums[write_ptr] = nums[read_ptr]

        return write_ptr + 1