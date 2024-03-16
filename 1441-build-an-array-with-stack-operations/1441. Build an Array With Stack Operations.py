class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        m = len(target)
        t_i = 0
        out = []
        for i in range(1, n+1):
            if target[t_i] == i:
                out.append("Push")
                t_i += 1
            else:
                out.append("Push")
                out.append("Pop")
            if t_i == m:
                break
        return out
