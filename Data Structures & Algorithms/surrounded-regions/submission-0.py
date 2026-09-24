class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        escaped = set()
        y = len(board)
        x = len(board[0])

        def dfs(r,c):
            if r < 0 or r >= y or c < 0 or c >= x or (r,c) in escaped:
                return 
            if board[r][c] != 'O':
                return
            escaped.add((r,c))
            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r - 1, c)

        for r in range(y):
            first_cell = board[r][0]
            last_cell = board[r][x - 1]
            if first_cell == 'O' and (r,0) not in escaped:
                dfs(r, 0)
            if last_cell == 'O' and (r,x-1) not in escaped:
                dfs(r, x-1)
        for c in range(x):
            first_cell = board[0][c]
            last_cell = board[y-1][c]
            if first_cell == 'O' and (0,c) not in escaped:
                dfs(0, c)
            if last_cell == 'O' and (y-1,c) not in escaped:
                dfs(y-1, c)
        # over-writing the matrix in-place
        for r in range(y):
            for c in range(x):
                if board[r][c] == 'O' and (r,c) not in escaped:
                    board[r][c] = 'X' 