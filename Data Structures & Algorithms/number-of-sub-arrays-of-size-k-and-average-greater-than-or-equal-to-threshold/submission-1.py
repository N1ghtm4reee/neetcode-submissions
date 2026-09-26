class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        r = k
        n = len(arr)
        res = 0
        while r <= n:
            sub = arr[l:r]
            avg = sum(sub) // k
            if avg >= threshold:
                res += 1
            r += 1
            l += 1
        return res