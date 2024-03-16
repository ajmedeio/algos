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

class WordDictionary:
    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.insert(word)
        

    def search(self, word: str) -> bool:
        out = False
        i = 0
        def dfs(n: Node):
            nonlocal out
            nonlocal i
            if out: # backtrack (prune) case
                return
            if i == len(word):
                if n.end:
                    out = True
                return
            c = word[i]
            if c != "." and c in n.children:
                i += 1
                dfs(n.children[c])
                i -= 1
            elif c == ".":
                i += 1
                for child_key in n.children:
                    dfs(n.children[child_key])
                i -= 1
        dfs(self.trie.root)
        return out
        