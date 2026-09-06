class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        print(intervals)
        res = []
        prev = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= prev[1]:
                prev[1] = max(intervals[i][1], prev[1])
            else:
                res.append(prev)
                prev = intervals[i]
        res.append(prev)
        return res