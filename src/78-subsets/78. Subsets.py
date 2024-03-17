class Solution:
    def subsets(self, A: List[int]) -> List[List[int]]:
        n, scratch, out = len(A), [], []

        def recurse(i):
            out.append(scratch.copy())

            for j in range(i, n):
                scratch.append(A[j])
                recurse(j+1)
                scratch.pop()

        recurse(0)
        return out