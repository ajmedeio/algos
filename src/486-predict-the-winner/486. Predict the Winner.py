class Solution:
    def PredictTheWinner(self, A: List[int]) -> bool:
        n = len(A)
        
        @cache
        def rec(lo, hi):
            if lo >= hi:
                return A[lo]
            return max(A[lo] - rec(lo+1, hi), A[hi] - rec(lo, hi-1))
        
        return rec(0, n-1) >= 0
