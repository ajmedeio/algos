class Solution:
    def nextGreaterElement(self, B: List[int], A: List[int]) -> List[int]:
        m = {}
        s = []
        out = []
        for e in A:
            while s and s[-1] < e:
                m[s.pop()] = e
            s.append(e)
        return [m.get(e, -1) for e in B]