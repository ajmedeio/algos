class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        A = nums
        for i in range(n):
            while A[i] != i+1:
                d = A[i] - 1
                if A[d] == A[i]:
                    break
                A[d], A[i] = A[i], A[d]
        
        out = []
        for i in range(n):
            if A[i] - 1 != i:
                out.append(A[i])
        return out