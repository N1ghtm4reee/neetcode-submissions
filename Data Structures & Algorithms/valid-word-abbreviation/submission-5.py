class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        l,r = 0, 0
        while l < len(word) and r < len(abbr):
            if abbr[r].isalpha():
                if word[l] != abbr[r]:
                    return False
                l += 1
                r += 1
                continue
            if abbr[r] == "0":
                return False
            k = r
            while r < len(abbr) and abbr[r].isdigit():
                    r += 1
            number = abbr[k:r]
            l += int(number)
        return l == len(word) and r == len(abbr)
