class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""
        t = num // 1000
        num %= 1000 
        for _ in range(t):
            roman += "M"

        h = num // 100
        num %= 100
        if h == 9:
            roman += "CM"
        elif h >= 5:
            roman += "D"
            for _ in range(h - 5):
                roman += "C"
        elif h == 4:
            roman += "CD"
        else:
            for _ in range(h):
                roman += "C"

        t = num // 10
        num %= 10
        if t == 9:
            roman += "XC"
        elif t >= 5:
            roman += "L"
            for _ in range(t - 5):
                roman += "X"
        elif t == 4:
            roman += "XL"
        else:
            for _ in range(t):
                roman += "X"

        if num == 9:
            roman += "IX"
        elif num >= 5:
            roman += "V"
            for _ in range(num - 5):
                roman += "I"
        elif num == 4:
            roman += "IV"
        else:
            for _ in range(num):
                roman += "I"

        return roman

# 2nd edition
# merge abundent code together
class Solution1:
    def intToRoman(self, num: int) -> str:
        roman = ""
        ones = ["M", "C", "X", "I"]
        fives = ["", "D", "L", "V"]
        tens = ["", "M", "C", "X"]

        for i in range(4):
            t = (10 ** (3 - i))
            digit = num // t
            num %= t
            if digit == 9:
                roman += (ones[i] + tens[i])
            elif digit >= 5:
                roman += fives[i]
                for _ in range(digit - 5):
                    roman += ones[i]
            elif digit == 4:
                roman += (ones[i] + fives[i])
            else:
                for _ in range(digit):
                    roman += ones[i]

        return roman
