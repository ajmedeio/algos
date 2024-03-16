class TrieNode:
    def __init__(self):
        self.children = {}

    def insert(self, word):
        curr = self
        for c in word:
            if c not in curr:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.children['$'] = None

    def __getitem__(self, item):
        return self.children[item]

    def __contains__(self, item):
        return item in self.children

def neighbors(board: List[List[str]], i, j, trie: TrieNode):
    out = []
    if i > 0:
        out.append((i-1, j))
    if i < (len(board) - 1):
        out.append((i+1, j))
    
    if j > 0:
        out.append((i, j-1))
    if j < (len(board[0]) - 1):
        out.append((i, j+1))

    return [(ni, nj) for ni, nj in out if board[ni][nj] != "." and board[ni][nj] in trie]

class Solution:
    def exists(self, board, trie_root: TrieNode) -> bool:
        m = len(board)
        n = len(board[0])
        
        def dfs(i, j, trie: TrieNode):
            c = board[i][j]
            board[i][j] = "."
            slate.append(c)
            if c in trie:
                if '$' in trie[c]:
                    completed.add("".join(slate))
                for ni, nj in neighbors(board, i, j, trie[c]):
                    dfs(ni, nj, trie[c])
            slate.pop()
            board[i][j] = c

        out = set()
        for i in range(m):
            for j in range(n):
                visited = set()
                completed = set()
                slate = []
                dfs(i, j, trie_root)
                out.update(set(completed))
        return out

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = TrieNode()
        for word in words:
            trie.insert(word)
        return self.exists(board, trie)
        