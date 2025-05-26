from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        num_rows = len(board)
        num_cols = len(board[0])
        border = set()

        def is_surrounded(matrix, row, col, visited):
            """
            Check the left, top, right, bottom cells to see if they are marked as "O".
            If they are, then mark them as Invalid.
            """
            if (row, col) not in visited:
                matrix[row][col] = "I"
                visited.add((row, col))
            else:
                return matrix
            # check left
            if col - 1 >= 0 and matrix[row][col-1] == "O":
                is_surrounded(matrix, row=row, col=col-1, visited=visited)
            # check top
            if row - 1 >= 0 and matrix[row-1][col] == "O":
                is_surrounded(matrix, row-1, col, visited)
            # check right
            if col + 1 < num_cols - 1 and matrix[row][col+1] == "O":
                is_surrounded(matrix, row, col+1, visited)
            if row + 1 < num_rows - 1 and matrix[row+1][col] == "O":
                is_surrounded(matrix, row+1, col, visited)
            return matrix

        # loop through the border rows and looks for "O"
        # then find the adjacent "O" cells and to mark them as invalid.
        for c in range(num_cols):
            if board[0][c] == "O":
                is_surrounded(board, 0, c, border)
            if board[num_rows-1][c] == "O":
                is_surrounded(board, num_rows-1, c, border)

        # cols
        for r in range(1, num_rows - 1):
            if board[r][0] == "O":
                is_surrounded(board, r, 0, border)
            if board[r][num_cols-1] == "O":
                is_surrounded(board, r, num_cols-1, border)

        for r in range(num_rows):
            for c in range(num_cols):
                if board[r][c] == "I":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
