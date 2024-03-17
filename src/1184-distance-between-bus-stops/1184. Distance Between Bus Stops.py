class Solution:
    def distanceBetweenBusStops(self, D: List[int], src: int, dst: int) -> int:
        if src > dst:
            src, dst = dst, src
        P = 0
        Psrc = 0
        Pdst = 0
        for i, d in enumerate(D):
            if i == src:
                Psrc = P
            if i == dst:
                Pdst = P
            P += d
        cw = Pdst - Psrc
        return min(cw, P - cw)
