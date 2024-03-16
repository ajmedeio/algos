class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        n = len(A)
        e, o = 0, 1
        while e < n and o < n:
            if A[e] % 2 == 0:
                e += 2
            elif A[o] % 2 == 1:
                o += 2
            else:
                A[e], A[o] = A[o], A[e]
                e += 2
                o += 2
        return A
