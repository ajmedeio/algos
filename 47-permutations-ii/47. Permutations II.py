class Solution:
    def permuteUnique(self, A: List[int]) -> List[List[int]]:
        A.sort()
        n, out, scratch = len(A), [], []
        U = [False] * n  # U for used
        def recurse():
            if len(scratch) == n:
                out.append(scratch.copy())
            
            for i in range(n):
                if U[i] or (i > 0 and A[i] == A[i-1] and not U[i-1]):
                    continue
                scratch.append(A[i])
                U[i] = True
                recurse()
                U[i] = False
                scratch.pop()

        recurse()
        return out