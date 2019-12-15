
# 476ms/52.07%
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        f_queries = [self.f(s) for s in queries]
        f_words = [self.f(s) for s in words]

        ans = []
        for i in f_queries:
            c = 0
            for j in f_words: 
                if i < j:
                    c += 1
            ans.append(c)

        return ans

    def f(self, s):
        min_word = 'z'
        count = 0
        for i in s:
            if i < min_word:
                min_word = i
                count = 1
            elif i == min_word:
                count += 1

        return count

