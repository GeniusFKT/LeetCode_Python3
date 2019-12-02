class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        for num in arr:
            if count.get(num) is None:
                count[num] = 1
            else:
                count[num] += 1

        for i in count.keys():
            for j in count.keys():
                if i != j and count[i] == count[j]:
                    return False
        
        return True