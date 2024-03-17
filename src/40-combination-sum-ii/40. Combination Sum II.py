class Solution:
    def combinationSum2(self, A: List[int], t: int) -> List[List[int]]:
        A.sort()
        n, scratch, sum_scratch, out = len(A), [], 0, []
        def recurse(i):
            nonlocal sum_scratch
            if sum_scratch == t:
                out.append(scratch[:])
                return
            if sum_scratch > t:
                return
            
            for j in range(i, n):
                if j > i and A[j] == A[j-1]:
                    continue
                scratch.append(A[j])
                sum_scratch += A[j]
                recurse(j+1)
                sum_scratch -= A[j]
                scratch.pop()

        recurse(0)
        return out
