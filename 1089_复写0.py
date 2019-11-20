
# 80ms/98%
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        fast_ptr = -1
        slow_ptr = -1
        arr_len = len(arr)
        flag = True

        # determine the ending index
        while fast_ptr < arr_len - 1:
            slow_ptr += 1
            if arr[slow_ptr] == 0:
                fast_ptr += 2
                flag = False
            else:
                fast_ptr += 1

        # handle exception
        if flag:
            return

        if fast_ptr == arr_len:
            arr[arr_len - 1] = 0
            slow_ptr -= 1
            fast_ptr = arr_len - 2

        # traverse the array reversely
        for ptr in range(slow_ptr, -1, -1):
            arr[fast_ptr] = arr[ptr]
            fast_ptr -= 1

            if arr[ptr] == 0:
                arr[fast_ptr] = 0
                fast_ptr -= 1
