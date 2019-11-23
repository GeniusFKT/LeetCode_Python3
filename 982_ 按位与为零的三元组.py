
# 4096ms/72.96%
# two for loops
class Solution:
    def countTriplets(self, A: List[int]) -> int:
        count = {}
        for i in A:
            for j in A:
                if count.get(i & j) is None:
                    count[i & j] = 1
                else:
                    count[i & j] += 1

        ans = 0
        for k in A:
            for key in count.keys():
                if k & key == 0:
                    ans += count[key]

        return ans