class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        res = 0
        window_size = 0
        window_sum = 0
        min_window_size = len(nums)
        l = 0
        for r, v in enumerate(nums):
            window_sum += v
            window_size = r - l + 1
            while window_sum >= target:
                window_size = r - l + 1
                if min_window_size >= window_size:
                    res = min_window_size = window_size
                window_sum -= nums[l]
                l += 1

        return res