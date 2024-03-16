class Node:
    def __init__(self):
        self.children = {}
        self.end = False
    
class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.end = True

class Solution:
    def longestCommonPrefix(self, words: List[str]) -> str:
        t = Trie()
        for word in words:
            t.insert(word)
        
        out = ""
        def dfs(n: Node):
            if n.end == True:
                return
            nonlocal out
            if len(n.children) == 1:
                for child in n.children:
                    c = child
                out += c
                dfs(n.children[c])

        dfs(t.root)
        return out
        