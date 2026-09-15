class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        grid_x, grid_y = len(grid[0]), len(grid)
        def find_island(grid, x, y):
            # dfs and map every visited vertex to a diff value "-1"
            nonlocal grid_x
            nonlocal grid_y
            if x >= grid_x or y >= grid_y or y < 0 or x < 0:
                return 
            if grid[y][x] == '-1' or grid[y][x] == '0':
                return
            if grid[y][x] == '1':
                grid[y][x] = '-1' # visited
            find_island(grid, x + 1, y)
            find_island(grid, x, y + 1)
            find_island(grid, x - 1, y)
            find_island(grid, x, y - 1)

        y = 0, 0
        for y in range(grid_y):
            for x in range(grid_x):
                if grid[y][x] == '1':
                    islands += 1
                    find_island(grid, x, y)
        return islands