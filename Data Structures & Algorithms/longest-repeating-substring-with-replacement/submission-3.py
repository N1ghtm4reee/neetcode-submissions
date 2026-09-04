class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        dup = {}
        res = 0
        max_freq = 0
        for r in range(len(s)):
            dup[s[r]] = dup.get(s[r], 0) + 1
            max_freq = max(max_freq, dup[s[r]])
            window = r - l + 1
            replacements = window - max_freq
            while replacements > k:
                dup[s[l]] -= 1
                l += 1
                window = r - l + 1
                replacements = window - max_freq
            res = max(res, window)
        return res