from heapq import (heapify, heappop, heappush)
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        res = []
        def distance(point: list[int]) -> int:
            return point[0] ** 2 + point[1] ** 2
        heap = [(-distance(point), i) for i, point in enumerate(points[:k])]
        heapify(heap)
        for i in range(k, len(points)):
            p_d = -distance(points[i])
            if p_d > heap[0][0]:
                heappop(heap)
                heappush(heap, (p_d, i))
        while heap:
            res.append(points[heappop(heap)[1]])
        return res