class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        found = set()
        n = len(candidates)
        def backTracking(comb: list[int], curr_sum, i):
            if curr_sum == target and tuple(comb) not in found: # base case
                res.append(comb.copy())
                found.add(tuple(comb))
            if curr_sum > target or i >= n:
                return
            curr_sum += candidates[i]
            comb.append(candidates[i])
            backTracking(comb, curr_sum, i)
            curr_sum -= candidates[i]
            comb.pop()
            backTracking(comb, curr_sum, i + 1)
        comb = []
        backTracking(comb, 0, 0)
        return res