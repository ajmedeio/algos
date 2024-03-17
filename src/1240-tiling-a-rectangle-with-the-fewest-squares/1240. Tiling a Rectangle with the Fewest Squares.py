class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        memo = {}
        def backtrack(a: int, ar: int,  b: int, br: int) -> int:
            """
            ar, br tracking the 'sunken' part of width and height
            """
            if a == b and ar == 0 and br == 0:
                # Base case, avoid further tiling
                return 1
            
            elif a < b:
                # maintains width(a) being the longer side
                return backtrack(b, br, a, ar)
            
            if ((a, ar, b, br) in memo):
                return memo[(a, ar, b, br)]
            
            res = a * b
            l = b - br
            
            # 1. Full Rectangle;
            if ar == br == 0:
                ## Explore all squares with length <= height (shorter one)
                for l in range(1, b+1):
                    res = min(res, 1 + backtrack(a, l, b, l))
                # return res
            elif br == b:
                # Essentially Full rectangle; note when br == b, b x b square was cut
                return backtrack(a-b, 0, b, 0)
            
            # 2. 'Sunken' Rectangle
            ## further tile the max remaining square along height
            elif l == ar:
                # a full rectangle
                res = 1 + backtrack(a-l, 0, b, 0)
            elif l < ar:
                res = 1 + backtrack(a-l, ar-l, b, br)
            elif l > ar:
                # note l < b < a
                res = 1 + backtrack(a-ar, l-ar, b, l)
                
            # print(f"Width: {a}, sunken: {ar}; Height: {b}, sunke: {br}; Result: {res}")
            memo[(a, ar, b, br)] = res
            return res
        
        return backtrack(n, 0,  m, 0)