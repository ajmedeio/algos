class Solution:
    def updateMatrix(self, M: List[List[int]]) -> List[List[int]]:
        def valid(r, c):
            return 0 <= r < n and 0 <= c < m
        out = [row[:] for row in M]
        n = len(M)
        m = len(M[0])
        q = deque()
        seen = set()

        for i in range(n):
            for j in range(m):
                if M[i][j] == 0:
                    q.append((i, j, 0))
                    seen.add((i, j))

        directions = [(-1, 0), (0, -1), (0, +1), (+1, 0)]
        
        while q:
            r, c, d = q.popleft()

            for dr, dc in directions:
                nx, ny = r + dr, c + dc
                if (nx, ny) not in seen and valid(nx, ny):
                    seen.add((nx, ny))
                    q.append((nx, ny, d + 1))
                    out[nx][ny] = d + 1
        
        return out
