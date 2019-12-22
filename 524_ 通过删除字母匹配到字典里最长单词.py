
# 384ms/55.96%
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        result = -1
        result_s = ""

        for sd in d:
            num = self._check(s, sd)
            if num > result:
                result_s = sd
                result = num
            elif num == result:
                if sd < result_s:
                    result_s = sd

        return result_s

    def _check(self, s, sd):
        ptr_slow = 0
        ptr_fast = 0
        for ptr_slow in range(len(sd)):
            try:
                while s[ptr_fast] != sd[ptr_slow]:
                    ptr_fast += 1
                ptr_fast += 1
            except IndexError:
                return -1

        return len(sd)


