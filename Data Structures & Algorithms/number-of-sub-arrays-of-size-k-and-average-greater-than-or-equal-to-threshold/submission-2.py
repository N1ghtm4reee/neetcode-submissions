class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        r = k
        n = len(arr)
        res = 0
        while r <= n:
            sub = arr[r-k:r]
            avg = sum(sub) // k
            if avg >= threshold:
                res += 1
            r += 1
        return res