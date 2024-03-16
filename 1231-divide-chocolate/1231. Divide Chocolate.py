class Solution:
    def maximizeSweetness(self, S: List[int], k: int) -> int:
        n = len(S)
        lo, hi = min(S), sum(S)
        while lo <= hi:
            i = lo + ((hi - lo) // 2)
            n_cuts = 0
            curr_sweetness = 0
            for j in range(n):
                curr_sweetness += S[j]
                if curr_sweetness >= i:
                    n_cuts += 1
                    curr_sweetness = 0
                    
            if n_cuts > k:
                lo = i + 1
            else:
                hi = i - 1
        return hi
