class Solution:
    def combinationSum(self, A: List[int], t: int) -> List[List[int]]:
        n, out, scratch, total = len(A), [], [], 0
        def recurse(i):
            nonlocal total
            if total >= t:
                if total == t:
                    out.append(scratch.copy())
                return
            if i == n:
                return

            for j in range(i, n):
                scratch.append(A[j])
                total += A[j]
                recurse(j)
                total -= A[j]
                scratch.pop()

        recurse(0)
        return out
