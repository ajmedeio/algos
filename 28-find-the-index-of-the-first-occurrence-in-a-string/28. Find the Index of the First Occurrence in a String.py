def trie_insert(root, word, start_index):
    curr = root
    for c in word:
        if c not in curr:
            curr[c] = {}
            curr[c]["start_index"] = set([start_index])
        else:
            curr[c]["start_index"].add(start_index)
        curr = curr[c]

class Solution:
    def strStr(self, T: str, P: str) -> int:
        n, m = len(T), len(P)
        root = {}
        for i in range(n):
            trie_insert(root, T[i:], i)

        curr = root
        for p in P:
            if p not in curr:
                return -1
            curr = curr[p]
        return min(curr["start_index"])
