class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        s = path[1:]
        ss = s.split('/')
        for token in ss:
            if '..' == token:
                if st:
                    st.pop()
            elif '.' == token:
                pass
            elif '' == token:
                pass
            else:
                st.append(token)
        return '/' + '/'.join(st)