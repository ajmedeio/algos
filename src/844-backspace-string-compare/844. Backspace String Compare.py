class Solution:
    def backspaceCompare3(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.zip_longest(F(S), F(T)))
    
    def backspaceCompare(self, s: str, t: str) -> bool:
        skipsS = 0
        skipsT = 0
        i = len(s) - 1
        j = len(t) - 1
        while i >= 0 or j >= 0:
            while i >= 0:
                if s[i] == "#":
                    skipsS += 1
                    i -= 1
                elif skipsS > 0:
                    skipsS -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if t[j] == "#":
                    skipsT += 1
                    j -= 1
                elif skipsT > 0:
                    skipsT -= 1
                    j -= 1
                else:
                    break
            
            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False
            if (i < 0 and j >= 0) or (i >= 0 and j < 0):
                return False
            
            i -= 1
            j -= 1
            
        return True
            
    
    def backspaceCompare2(self, s: str, t: str) -> bool:
        ls = []
        lt = []
        for i, cs in enumerate(s):
            if cs == "#": 
                if len(ls) > 0:
                    ls.pop()
            else:
                ls.append(cs)
                
        for i, ct in enumerate(t):
            if ct == "#": 
                if len(lt) > 0:
                    lt.pop()
            else:
                lt.append(ct)
        
        print("ls" + str(ls))
        print("lt" + str(lt))
        return ls == lt
                