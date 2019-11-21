import math

# 36ms/88.89% 
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        ratio = minutesToTest // minutesToDie + 1
        return math.ceil(math.log(buckets) / math.log(ratio))