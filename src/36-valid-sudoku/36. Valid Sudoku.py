

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        s = [0] * n

        # check the rows
        for r in range(n):
            s = [0] * n
            for c in range(n):
                if not board[r][c].isdigit():
                    continue
                i = int(board[r][c]) - 1
                if s[i] == 1:
                    return False
                s[i] = 1

        for r in range(n):
            s = [0] * n
            for c in range(n):
                if not board[c][r].isdigit():
                    continue
                i = int(board[c][r]) - 1
                if s[i] == 1:
                    return False
                s[i] = 1
        
        for r in range(3):
            for c in range(3):
                s = [0] * n
                for i in range(r * 3, (r+1) * 3):
                    for j in range(c * 3, (c+1) * 3):
                        if not board[i][j].isdigit():
                            continue
                        e = int(board[i][j]) - 1
                        if s[e] == 1:
                            return False
                        s[e] = 1

        return True  

        