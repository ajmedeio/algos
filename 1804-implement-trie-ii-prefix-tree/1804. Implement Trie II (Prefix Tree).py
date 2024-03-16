class Node:
    def __init__(self):
        self.children = {}
        self.under = 0
        self.count = 0

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            curr.under += 1
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.count += 1
        curr.under += 1

    def countWordsEqualTo(self, word: str) -> int:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return 0
            curr = curr.children[c]
        return curr.count

    def countWordsStartingWith(self, prefix: str) -> int:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return 0
            curr = curr.children[c]
        return curr.under

    def erase(self, word: str) -> None:
        curr = self.root
        for c in word:
            curr.under = max(0, curr.under - 1)
            if curr.children[c].under == 1:
                del curr.children[c]
                return
            curr = curr.children[c]
        curr.under = max(0, curr.under - 1)
        curr.count = max(0, curr.count - 1)
