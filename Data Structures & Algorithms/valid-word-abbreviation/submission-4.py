class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        l = 0
        r = 0
        while l < len(word):
            if abbr[r].isalpha() and abbr[r] == word[l]:
                r += 1
                l += 1
                continue
            elif abbr[r].isalpha() and abbr[r] != word[l]:
                return False
            k = r
            if abbr[r].isdigit() and abbr[r] == "0":
                return False
            while r < len(abbr) and abbr[r].isdigit():
                r += 1
            number = abbr[k:r]
            n = int(number)
            l += n
            if l < len(word) and word[l] != abbr[r]:
                return False
            elif l > len(word):
                return False
        return l == len(word) and r == len(abbr)