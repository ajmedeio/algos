class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        sorted_pairs = sorted(pairs, key=lambda p: p[1])
        prev_e = -math.inf
        n_chain = 0
        for s, e in sorted_pairs:
            if prev_e < s:
                n_chain += 1
                prev_e = e
        return n_chain
