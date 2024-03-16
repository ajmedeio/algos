class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = Node()
        self.root.end = True

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.end = True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        t = Trie()
        for word in words:
            t.insert(word)

        out = ""
        slate = []
        def dfs(n: Node):
            if n.end == False:
                return
            nonlocal out
            stone = "".join(slate)
            if len(out) < len(stone):
                out = stone
            if len(out) == len(stone) and stone < out:
                out = stone
            
            for c in n.children:
                slate.append(c)
                dfs(n.children[c])
                slate.pop()

        dfs(t.root)
        return out
        