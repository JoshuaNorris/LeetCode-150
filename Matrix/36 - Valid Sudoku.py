class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Variables
        seen = set()

        # Check Rows
        for r in range(9):
            for i in range(9):
                if board[r][i] in seen:
                    return False
                if board[r][i] != '.':
                    seen.add(board[r][i])
            seen = set()

        # Check columns
        for c in range(9):
            for i in range(9):
                if board[i][c] in seen:
                    return False
                if board[i][c] != '.':
                    seen.add(board[i][c])
            seen = set()

        # Check boxes
        for c in range(3):
            for r in range(3):
                for i in range(9):
                    row = (i // 3) + (r * 3)
                    column = (i % 3) + (c * 3)
                    if board[row][column] in seen:
                        return False
                    if board[row][column] != '.':
                        seen.add(board[row][column])
                seen = set()
            
        return True
                    
