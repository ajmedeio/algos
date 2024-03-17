from heapq import heapify, heappush, heappop

class Node:
    def __init__(self):
        self.children = {}
        self.end = False
        self.freq = 0

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word, freq):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.end = True
        curr.freq += freq

    def find_prefix(self, prefix) -> Node:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return None
            curr = curr.children[c]
        return curr


class HeapNode:
    def __init__(self, freq, fragment):
        self.freq = freq
        self.fragment = fragment
    
    def __lt__(self, other):
        if self.freq < other.freq:
            return True
        elif self.freq == other.freq and self.fragment > other.fragment:
            return True
        return False


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.search = ""
        self.trie = Trie()
        for i in range(len(sentences)):
            self.trie.insert(sentences[i], times[i])

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.trie.insert(self.search, 1)
            self.search = ""
            return []
        else:
            self.search += c
        
        h = []
        scratch = []
        def dfs(n: Node):
            if n is None:
                return
            if n.end == True:
                stone = "".join(scratch)
                heappush(h, HeapNode(n.freq, stone))
                if len(h) > 3:
                    heappop(h)
            # recurse
            for child in n.children:
                scratch.append(child)
                dfs(n.children[child])
                scratch.pop()

        scratch = [l for l in self.search]
        dfs(self.trie.find_prefix(self.search))
        out = []
        while h:
            out.append(heappop(h).fragment)
        return list(reversed(out))
