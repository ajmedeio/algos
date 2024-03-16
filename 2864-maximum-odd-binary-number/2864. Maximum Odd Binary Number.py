class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # count the ones and zeros
        # place all the ones but a single on the left hand side, fill the rest with zeros and then place the last slot as a one.
        n_z = s.count("0")
        n_o = s.count("1")
        out = ["0"] * (n_z + n_o)
        for i in range(n_o-1):
            out[i] = "1"
        out[-1] = "1"
        return "".join(out)