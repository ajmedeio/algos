class Solution:
    def sortColors(self, A: List[int]) -> None:
        v = 1
        lt, i, gt = 0, 0, len(A)-1
        while i <= gt:
            if A[i] < v:
                A[i], A[lt] = A[lt], A[i]
                lt += 1
                i += 1
            elif A[i] > v:
                A[i], A[gt] = A[gt], A[i]
                gt -= 1
            elif A[i] == v:
                i += 1
