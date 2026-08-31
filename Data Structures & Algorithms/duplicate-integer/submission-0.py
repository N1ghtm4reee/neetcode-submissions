class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        size = len(nums)
        i = 0
        while i < size - 1:
            j = i + 1
            while j < size:
                if nums[i] == nums[j]:
                    return True
                j += 1
            i += 1
        return False