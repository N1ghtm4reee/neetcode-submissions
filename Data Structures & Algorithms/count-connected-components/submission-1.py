class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # for each vertex we are going to use union find
        # by trying to find the represent of every vertex if not found increment the res as the count of groups we have
        if n == 0:
            return 0
        parents = [i for i in range(n)]
        res = n
        def find_union(v) -> int:
            if parents[v] == v:
                return v
            return find_union(parents[v])
        for i in range(len(edges)):
            a = find_union(edges[i][0])
            b = find_union(edges[i][1])
            parents[b] = a
            if a != b:
                res -= 1
        return res