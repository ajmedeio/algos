class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        l = m+n
        i, j, k = m-1, n-1, l-1
        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                A[k] = A[i]
                i -= 1
            elif A[i] < B[j]:
                A[k] = B[j]
                j -= 1
            else:
                A[k] = A[i]
                i -= 1
            k -= 1
        while i >= 0:
            A[k] = A[i]
            i -= 1
            k -= 1
        while j >= 0:
            A[k] = B[j]
            j -= 1
            k -= 1
        