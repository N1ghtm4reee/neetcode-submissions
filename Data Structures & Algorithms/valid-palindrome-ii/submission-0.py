class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrom(l, r) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        l,r = 0, len(s) - 1
        deleted = False
        while l < r:
            if s[l] != s[r]:
                return isPalindrom(l + 1, r) or isPalindrom(l, r - 1)
            l += 1
            r -= 1
        return True
