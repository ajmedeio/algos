class Solution:
    def removeElement(self, A: List[int], val: int) -> int:
        i, j = 0, len(A) - 1
        while i <= j:
            if A[i] == val:
                A[i] = A[j]
                j -= 1
            else:
                i += 1
        return j + 1
