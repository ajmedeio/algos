class Solution(object):
    def minmaxGasDist(self, S, k):
        tolerance = 10 ** (-6)
        n = len(S)
        ds = []
        for i in range(1, n):
            ds.append(S[i] - S[i-1])
        lo, hi = 0, max(ds)
        while lo <= hi - tolerance:
            i = lo + ((hi - lo) / 2)
            n_new = 0
            for d in ds:
                n_new += ceil(d / i) - 1
            if n_new > k:
                lo = i
            else:
                hi = i
        return lo
