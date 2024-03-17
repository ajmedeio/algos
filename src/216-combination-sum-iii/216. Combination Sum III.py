class Solution:
    def combinationSum3(self, k: int, t: int) -> List[List[int]]:
        A = [i for i in range(1,10)]
        n = len(A)
        out = []
        scratch = []
        total = 0
        def recurse(i):
            nonlocal total
            if len(scratch) >= k or total >= t:
                if total == t and len(scratch) == k:
                    out.append(scratch.copy())
                return
            
            for j in range(i, n):
                scratch.append(A[j])
                total += A[j]
                recurse(j+1)
                total -= A[j]
                scratch.pop()

        recurse(0)
        return out