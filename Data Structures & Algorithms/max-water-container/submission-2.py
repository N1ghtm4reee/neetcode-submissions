class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res, curRes = 0, 0
        l, r = 0, len(heights) - 1
        while (l < r):
            curRes = min(heights[l], heights[r]) * (r - l)
            res = max(res, curRes)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return res