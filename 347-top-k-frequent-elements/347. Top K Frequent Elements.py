class Solution:
    def topKFrequent(self, A: List[int], k: int) -> List[int]:
        # count frequencies and bucket sort
        counter = Counter(A)
        n_buckets = -inf
        for e, f in counter.items():
            n_buckets = max(n_buckets, f)
        buckets = [[]] * (n_buckets + 1)
        for e, f in counter.items():
            if len(buckets[f]) == 0:
                buckets[f] = [e]
            else:
                buckets[f].append(e)
        out = []
        i = n_buckets
        while i >= 0 and len(out) < k:
            for e in buckets[i]:
                out.append(e)
            i -= 1
        return out
