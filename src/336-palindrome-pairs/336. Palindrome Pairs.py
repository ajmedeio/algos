class Trie:
    def __init__(self):
        self.children = {"$": None}
    
    def insert(self, s):
        curr = self
        for letter in s:
            child = Trie()
            curr.children[letter] = child
            curr = child
        curr.children["$"] = None
        return self
    
    def __str__(self):
        out = defaultdict(lambda: [])
        q = [(0, self)]
        while q:
            level, v = q.pop()
            for k, t in v.children.items():
                if k == "$":
                    continue
                out[level].append(k)
                q.append((level+1, t))
        return str(out)


def is_palindrome(s):
    i, j = 0, len(s)-1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        out = []
        D = {word: i for i, word in enumerate(words)}
        if "" in D:
            for i, word in enumerate(words):
                if word == "":
                    continue
                if is_palindrome(word):
                    out.append((D[""], i))
                    out.append((i, D[""]))

        for word, i in D.items():
            l = len(word)
            back_word = word[::-1]
            if back_word in D and D[back_word] != i:
                out.append((i, D[back_word]))

            for k in range(1, l):
                prefix = word[0:k]
                suffix = word[k:l]
                back_prefix = prefix[::-1]
                if back_prefix in D and D[back_prefix] != i:
                    if is_palindrome(suffix):
                        out.append((i, D[back_prefix]))

            for k in range(1, l):
                prefix = word[0:k]
                suffix = word[k:l]
                back_suffix = suffix[::-1]
                if back_suffix in D and D[back_suffix] != i:
                    if is_palindrome(prefix):
                        out.append((D[back_suffix], i))
        return out
