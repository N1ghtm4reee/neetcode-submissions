class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[-1]
        while l <= r:
            mid = l + (r - l) // 2
            res = min(res, nums[mid])
            if nums[mid] < nums[r]: # min val may be in the left part
                r = mid
            else:
                l = mid + 1
        return res