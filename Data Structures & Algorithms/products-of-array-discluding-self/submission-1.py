class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        prefix = [nums[0]] * n
        suffix = [nums[n - 1]] * n
        for l in range(1, n):
            prefix[l] = nums[l] * prefix[l - 1]
        for r in range(n - 2 , -1, -1):
            suffix[r] = nums[r] * suffix[r + 1]
        res = [1] * n
        for i in range(n):
            if i == 0:
                res[i] = suffix[i + 1]
            elif i == n - 1:
                res[i] = prefix[i - 1]
            else:
                res[i] = prefix[i - 1] * suffix[i + 1]
        return res