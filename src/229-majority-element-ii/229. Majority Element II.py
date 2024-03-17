class Solution:
    def majorityElement(self, A: List[int]) -> List[int]:
        n = len(A)
        m = {}
        for i in range(n):
            if len(m) < 2:
                m[A[i]] = m.get(A[i], 0) + 1
            elif len(m) >= 2:
                if A[i] in m:
                    m[A[i]] += 1
                else:
                    to_delete = []
                    for k in m.keys():
                        m[k] -= 1
                        if m[k] == 0:
                            to_delete.append(k)
                    for k in to_delete:
                        del m[k]
        for k in m:
            m[k] = 0
        for a in A:
            if a in m:
                m[a] += 1
        out = []
        for k in m:
            if m[k] > (n//3):
                out.append(k)
        return out
