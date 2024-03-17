class Solution:
    def bestClosingTime(self, C: str) -> int:
        n = len(C)
        s = 0
        m = 0
        m_i = -1
        for i in range(n):
            if C[i] == 'Y':
                s += 1
            else:
                s -= 1
            if s > m:
                m, m_i = s, i
        return m_i + 1