class Solution:
    def findNumberOfLIS(self, A: List[int]) -> int:
        n = len(A)
        length = [1] * n
        count = [1] * n
        
        for i in range(n):
            for j in range(i):
                if A[j] < A[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = 0
                    if length[j] + 1 == length[i]:
                        count[i] += count[j]
        
        max_length = max(length)
        result = 0
        
        for i in range(n):
            if length[i] == max_length:
                result += count[i]
        
        return result