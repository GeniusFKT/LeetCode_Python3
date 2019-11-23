
# 96ms/99.32%
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        tmp = []
        for interval in intervals:
            if tmp == []:
                tmp = interval
            else:
                if tmp[1] < interval[0]:
                    ans.append(tmp)
                    tmp = interval
                else:
                    if tmp[1] < interval[1]:
                        tmp[1] = interval[1]

        if tmp != []:
            ans.append(tmp)

        return ans