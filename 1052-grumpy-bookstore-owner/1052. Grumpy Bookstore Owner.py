class Solution:
    def maxSatisfied(self, A: List[int], g: List[int], k: int) -> int:
        n = len(A)
        T = sum(A[0:k])
        for i in range(k, n):
            if g[i] == 0:
                T += A[i]
        T_max = T
        for i in range(k, n):
            T -= A[i-k] if g[i-k] == 1 else 0
            T += A[i] if g[i] == 1 else 0
            T_max = max(T_max, T)    
        return T_max
