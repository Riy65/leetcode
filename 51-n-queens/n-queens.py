class Solution:
    def solveNQueens(self, n: int):
        result = []
        board = [["."] * n for _ in range(n)]

        cols = set()
        posDiag = set()   # row + col
        negDiag = set()   # row - col

        def backtrack(row):
            if row == n:
                result.append(["".join(r) for r in board])
                return

            for col in range(n):
                if col in cols or (row + col) in posDiag or (row - col) in negDiag:
                    continue

                # Place queen
                cols.add(col)
                posDiag.add(row + col)
                negDiag.add(row - col)
                board[row][col] = "Q"

                backtrack(row + 1)

                # Backtrack
                cols.remove(col)
                posDiag.remove(row + col)
                negDiag.remove(row - col)
                board[row][col] = "."

        backtrack(0)
        return result
        