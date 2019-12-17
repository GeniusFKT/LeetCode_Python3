
# 168ms/88.95%
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        d = {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1}
        for i in range(0, n - 1):
            d_new = {}
            d_new["a"] = (d["e"] + d["i"] + d["u"]) % (10 ** 9 + 7)
            d_new["e"] = (d["a"] + d["i"]) % (10 ** 9 + 7)
            d_new["i"] = (d["e"] + d["o"]) % (10 ** 9 + 7)
            d_new["o"] = d["i"]
            d_new["u"] = (d["o"] + d["i"]) % (10 ** 9 + 7)

            d = d_new

        return (sum(d.values())) % (10 ** 9 + 7)
