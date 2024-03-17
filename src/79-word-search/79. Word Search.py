def neighbors(board: List[List[str]], i, j):
    out = []
    if i > 0:
        out.append((i-1, j))
    if i < (len(board) - 1):
        out.append((i+1, j))
    
    if j > 0:
        out.append((i, j-1))
    if j < (len(board[0]) - 1):
        out.append((i, j+1))
    return out

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        l = len(word)
        
        def dfs(i, j, k):
            visited.add((i,j))
            result = False
            if board[i][j] == word[k] and k == l-1:
                return True
            if board[i][j] == word[k]:
                for nei in neighbors(board, i, j):
                    if nei not in visited:
                        result |= dfs(nei[0], nei[1], k+1)
                        if result:  # once true, always true
                            return result
            visited.remove((i,j))
            return result

        out = False
        for i in range(m):
            for j in range(n):
                visited = set()
                out |= dfs(i, j, 0)
                if out:
                    return out # once true, always true
        return out
