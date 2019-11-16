import numpy as np
class Solution1:
    def heightChecker(self, heights: list[int]) -> int:
        tmp = np.array(heights)
        heights.sort()

        cnt = 0
        for i in range(len(heights)):
            if tmp[i] != heights[i]:
                cnt += 1

        return cnt

class Solution2:
    def heightChecker(self, heights: list[int]) -> int:
        tmp = np.zeros([101])
        for i in heights:
            tmp[i] += 1

        idx = 0
        cnt = 0
        length = len(heights)
        for i in range(len(tmp)):
            if tmp[i] == 0:
                continue
            for _ in range(int(tmp[i])):
                if heights[idx] != i:
                    cnt += 1
                idx += 1
            if idx == length:
                break

        return cnt
