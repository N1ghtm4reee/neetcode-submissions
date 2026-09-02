class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # fast and slow pointers
        f, s = 0, 0
        while max(f,s) < len(nums):
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                break
        s = 0
        while s != f:
            s = nums[s]
            f = nums[f]
        return s