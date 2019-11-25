
# 48ms/70.76%
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word_list = []
        word = ""
        flag = False
        for letter in paragraph:
            if letter.isalpha():
                word += letter
                flag = True
            else:
                if flag:
                    word_list.append(word.lower())
                    word = ""
                    flag = False

        if word != "":
            word_list.append(word.lower())

        count = {}
        for word in word_list:
            if count.get(word) is None:
                count[word] = 1
            else:
                count[word] += 1

        for word in banned:
            if count.get(word) is not None:
                count.pop(word)

        max_count = max(count.values())
        for key in count.keys():
            if count[key] == max_count:
                return key
