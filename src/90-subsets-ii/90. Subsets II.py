class Solution:
    def subsetsWithDup(self, A: List[int]) -> List[List[int]]:
        A.sort()
        n = len(A)
        out = []
        scratch = []
        def recurse(i):
            out.append(scratch.copy())

            for j in range(i, n):
                if j > i and A[j] == A[j-1]:
                    continue
                scratch.append(A[j])
                recurse(j+1)
                scratch.pop()

        recurse(0)
        return out
