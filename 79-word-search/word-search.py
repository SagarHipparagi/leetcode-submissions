class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows = len(board)
        cols = len(board[0])

        path = set()

        def dfs(r, c, i):
            # We found the complete word
            if i == len(word):
                return True

            # Invalid position or wrong character
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != word[i] or
                (r, c) in path):
                return False

            # Mark this cell as visited
            path.add((r, c))

            # Search up, down, left, right
            result = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )

            # Backtrack
            path.remove((r, c))

            return result

        # Try every cell as the starting point
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False