class Solution:
    def majorityElement(self, A: List[int]) -> int:
        n = len(A)
        major, c = 0, 0
        for i in range(n):
            if c == 0:
                major = A[i]
            c += +1 if A[i] == major else -1
        return major
