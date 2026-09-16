class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        y_length = len(board)
        x_length = len(board[0])

        if len(word) > y_length * x_length:
            return False

        visited = set()
        current_word = []

        def dfs(y, x, k) -> bool:
            if k == len(word):
                return True
            if y < 0 or y >= y_length or x < 0 or x >= x_length:
                return False
            if (y, x) in visited:
                return False
            if board[y][x] != word[k]:
                return False
            current_word.append(board[y][x])
            visited.add((y, x))
            # RIGHT
            if dfs(y, x + 1, k + 1):
                return True

            # LEFT
            if dfs(y, x - 1, k + 1):
                return True

            # DOWN
            if dfs(y + 1, x, k + 1):
                return True

            # UP
            if dfs(y - 1, x, k + 1):
                return True

            # Backtrack
            current_word.pop()
            visited.remove((y, x))

            return False

        for y in range(y_length):
            for x in range(x_length):
                if board[y][x] == word[0]:
                    if dfs(y, x, 0):
                        return True

        return False