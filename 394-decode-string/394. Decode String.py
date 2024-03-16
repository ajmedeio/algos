class Solution:
    def decodeString(self, s: str) -> str:
        res = []
        ss = ''
        for l in s:
            if l != ']':
                res.append(l)
            else:
                while res[-1] != '[':
                    ss = res.pop() + ss
                res.pop()
                
                digits = ''
                while res and res[-1].isdigit():
                    digits = res.pop() + digits
                res.append(ss * int(digits))
                ss = ""
        return ''.join(res)
                
        
        
        
    def tokenize(self, s: str) -> List[Tuple[str, str]]:
        out = []
        i = 0
        while i < len(s):
            number = re.search("^[0-9]+", s[i:])
            alpha = re.search("^[a-z]+", s[i:])
            newContext = re.search("^\[", s[i:])
            endContext = re.search("^\]", s[i:])
            if number:
                k = int(number.group(0))
                nDigits = number.span()[1] - number.span()[0]
                out.append(("number", k))
                i += nDigits
            elif alpha:
                nChars = alpha.span()[1] - alpha.span()[0]
                out.append(("alpha", alpha.group(0)))
                i += nChars
            elif newContext:
                out.append(("newContext", "["))
                i += 1
            elif endContext:
                out.append(("endContext", "]"))
                i += 1
        return out
    
    def decodeString2(self, s: str) -> str:
        tokens = self.tokenize(s)
        stacks = defaultdict(lambda: defaultdict(lambda: []))
        depth = 0
        stackNumber = 0
        for t, v in tokens:
            parent = (depth-1, len(stacks[stackNumber][depth-1]) - 1) if depth > 0 and len(stacks[stackNumber][depth-1]) > 0 else None
            if t == "number":
                stacks[stackNumber][depth].append((t, v, parent))
                depth += 1
            elif t == "alpha":
                stacks[stackNumber][depth].append((t, v, parent))
            elif t == "newContext":
                continue
            elif t == "endContext":
                depth -= 1
            if depth == 0:
                stackNumber += 1
        out = ""
        ss = ""
        for i, (index, stack) in enumerate(stacks.items()):
            for depth in range(len(stack) - 1, -1, -1):
                for n in range(len(stack[depth]) - 1, -1, -1):
                    (t, v, p) = stack[depth][n]
                    lookahead = stack[depth][n-1] if n-1 >= 0 else None
                    if lookahead and lookahead[2] == p:
                        stack[depth][n-1] = ("alpha", lookahead[1] + v, p)
                    elif p:
                        k = int(stack[p[0]][p[1]][1])
                        l = v * k
                        stack[p[0]][p[1]] = ("alpha", l, stack[p[0]][p[1]][2])
                    else:
                        ss = v
            out += ss
            ss = ""
        return out
