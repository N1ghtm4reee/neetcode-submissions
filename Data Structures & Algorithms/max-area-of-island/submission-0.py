class Solution:
    def get_area(self, grid, r, c, n_r, n_c, t_area) -> int:
        if r < 0 or c < 0 or r >= n_r or c >= n_c:
            return t_area
        if grid[r][c] == 0 or grid[r][c] == -1:
            return t_area
        t_area += 1
        grid[r][c] = -1
        t_area = self.get_area(grid, r, c + 1, n_r, n_c, t_area)
        t_area = self.get_area(grid, r, c - 1, n_r, n_c, t_area)
        t_area = self.get_area(grid, r + 1, c, n_r, n_c, t_area)
        t_area = self.get_area(grid, r - 1, c, n_r, n_c, t_area)
        return t_area
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n_r = len(grid)
        n_c = len(grid[0])
        area = 0
        for r in range(n_r):
            for c in range(n_c):
                if grid[r][c] == 1:
                    t_area = self.get_area(grid, r, c, n_r, n_c, 0)
                    print(f"t_area: {t_area}")
                    area = max(area, t_area)
        return area
    
