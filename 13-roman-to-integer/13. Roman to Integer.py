class Solution:
    def romanToInt(self, s: str) -> int:
        singles = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        doubles = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }
        i, n, out = 0, len(s), 0
        while i < n:
            if (i+1) < n and s[i:i+2] in doubles:
                out += doubles[s[i:i+2]]
                i += 2
            else:
                out += singles[s[i]]
                i += 1
        return out
