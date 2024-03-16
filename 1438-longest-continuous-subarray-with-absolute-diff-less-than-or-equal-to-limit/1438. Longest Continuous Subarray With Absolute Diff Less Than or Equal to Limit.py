from collections import deque

class Solution:
    def longestSubarray(self, A: List[int], k: int) -> int:
        n = len(A)
        q_inc = deque()
        q_dec = deque()
        l = 0
        w = 0
        for i in range(n):
            while q_inc and A[i] < q_inc[-1][1]:
                q_inc.pop()
            while q_dec and A[i] > q_dec[-1][1]:
                q_dec.pop()
            q_inc.append((i, A[i]))
            q_dec.append((i, A[i]))
            
            # we have two properly built min/max queue incorporating the new element
            # now we move the left pointer while diff > k
            while q_dec[0][1] - q_inc[0][1] > k:
                if q_inc and q_inc[0][0] == l:
                    q_inc.popleft()
                if q_dec and q_dec[0][0] == l:
                    q_dec.popleft()
                l += 1
            w = max(w, i-l+1)
        return w
            
