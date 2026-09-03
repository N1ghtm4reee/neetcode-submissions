class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dup = {}
        j = 0
        longest = 0
        for i in range(len(s)):
            if s[i] in dup:
                j = max(j, dup[s[i]] + 1)
            longest = max(longest, i - j + 1)
            dup[s[i]] = i
        return longest

