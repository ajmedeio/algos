class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ascii_offset = 65
        q = columnNumber
        out = ""
        while q > 0:
            q -= 1
            q, r = q // 26, q % 26
            out += chr(r + ascii_offset)
        return "".join(reversed(out))
