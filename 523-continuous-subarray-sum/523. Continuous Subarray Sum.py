class Solution:
    def checkSubarraySum(self, A: List[int], k: int) -> bool:
        n = len(A)
        p = 0
        c = {0: 0}
        for i in range(n):
            p = p + A[i]
            if p % k in c:
                if i+1 - c[p % k] >= 2:
                    return True
            if p % k not in c:
                c[p % k] = i+1
        return False
