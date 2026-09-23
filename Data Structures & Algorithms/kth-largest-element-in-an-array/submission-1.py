from heapq import heappop, heappush, heapify
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # min heap
        # store up to k elements on the heap and return the first element as a res
        n = len(nums)
        heap = [num for num in nums[:k]]
        heapify(heap)
        for num in nums[k:]:
            if num > heap[0]:
                heappop(heap)
                heappush(heap, num)
        return heap[0]