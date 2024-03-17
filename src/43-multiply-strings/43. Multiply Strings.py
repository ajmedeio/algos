class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        out = 0
        carry = 0
        part = 0
        place = ""
        currPlace = 0
        line = ""
        for i1 in range(len(num1) - 1, -1, -1):
            n1 = num1[i1]
            for i2 in range(len(num2) - 1, -1, -1):
                n2 = num2[i2]
                part = str((int(n1) * int(n2)) + carry) 
                carry, place = (int(part[0]), part[-1]) if len(part) > 1 else (0, part[0])
                line = place + line if place != 0 else line
            part = int(str(carry) + line)
            line = ""
            carry = 0
            part *= 10**currPlace
            out += part
            currPlace += 1
                
        return str(out)
                