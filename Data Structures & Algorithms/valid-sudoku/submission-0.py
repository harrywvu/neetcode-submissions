class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sudokuRows = [
            set(),
            set(),
            set(),
            set(),
            set(),
            set(),
            set(),
            set(),
            set(),
        ]

        sudokuCols = [
            set(),
            set(),
            set(),
            set(),
            set(),
            set(),
            set(),
            set(),
            set(),
        ]

        sudokuSquares = [
            set(),  # 0, 0
            set(),  # 0, 1
            set(),  # 0, 2
            set(),  # 1, 0
            set(),  # 1, 1
            set(),  # 1, 2
            set(),  # 2, 0
            set(),  # 2, 1
            set(),  # 2, 2
        ]        
        
        # turn all rows into a set, return false if duplicates exist
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == ".": continue

                if board[row][col] in sudokuRows[row]:
                    return False

                sudokuRows[row].add(board[row][col])

        # turn all cols into a set, return false if duplicates exist
        for col in range(len(board)):
            for row in range(len(board)):
                if board[row][col] == ".": continue
                
                if board[row][col] in sudokuCols[col]:
                    return False

                sudokuCols[col].add(board[row][col])

        # check individual squares, return false if duplicates exist
        for r in range(len(board)):
            for c in range(len(board)):
                
                box_row = r // 3
                box_col = c // 3
                square_index = box_row * 3 + box_col

                if board[r][c] == ".": continue

                if board[r][c] in sudokuSquares[square_index]:
                    return False

                sudokuSquares[square_index].add(board[r][c])
        return True