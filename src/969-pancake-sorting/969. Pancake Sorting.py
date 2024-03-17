class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        n = len(A)
        A = A
        out = []
        for i in range(1, n+1):
            m, m_i = -inf, 0
            for j in range(0, n-i+1):
                if m < A[j]:
                    m, m_i = A[j], j
            if m_i+1 != n-i+1:
                A[0:m_i+1] = list(reversed(A[0:m_i+1]))
                A[0:n-i+1] = list(reversed(A[0:n-i+1]))
                out.append(m_i+1)
                out.append(n-i+1)
        return out
