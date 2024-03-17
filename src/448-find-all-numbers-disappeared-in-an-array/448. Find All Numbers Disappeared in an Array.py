class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        A = nums
        n = len(A)
        for i in range(n):
            while A[i] != i+1:
                d = A[i] - 1
                if A[i] == A[d]:
                    break
                A[i], A[d] = A[d], A[i]
        
        out = []
        for i in range(n):
            if A[i] != i+1:
                out.append(i + 1)
        return out