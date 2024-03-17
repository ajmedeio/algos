class Solution:
    def permute(self, A: List[int]) -> List[List[int]]:
        slate = []
        out = []
        used = [False] * len(A)
        def rec(level):
            if level == len(A):
                out.append(slate.copy())
                return
            
            for i in range(len(A)):
                if used[i] is False:
                    slate.append(A[i])
                    used[i] = True
                    rec(level + 1)
                    slate.pop()
                    used[i] = False

        rec(0)
        return out