from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        max_heap = []
        for key in freq:
            if len(max_heap) >= k:
                if freq[key] > max_heap[0][0]:
                    heappop(max_heap)
                    heappush(max_heap, (freq[key], key))
            else:
                heappush(max_heap, (freq[key], key))
        res = []
        while len(max_heap):
            res.append(heappop(max_heap)[1])
        return res