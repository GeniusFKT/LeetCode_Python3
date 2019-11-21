# 44ms/76.66%
# recursive
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        def _generateMatrix(start, n):
            if n == 1:
                return [[start]]
            if n == 2:
                return [[start, start + 1], [start + 3, start + 2]]
            center = _generateMatrix(start + 4 * (n - 1), n - 2)
            ans = []
            ans.append([idx for idx in range(start, start + n)])
            for i in range(n - 2):
                center[i].append(start + n + i)
                center[i].insert(0, start + 4 * n - 5 - i)
                ans.append(center[i])
            ans.append([idx for idx in range(start + 3 * (n - 1), start + 2 * (n - 1) - 1, -1)])
            return ans                
        return _generateMatrix(1, n)