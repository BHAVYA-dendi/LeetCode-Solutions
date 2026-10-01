class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m, n = len(heights), len(heights[0])

        def dfs(r, c, seen):
            seen.add((r, c))

            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r + dr, c + dc

                if (0 <= nr < m and 0 <= nc < n and
                    (nr, nc) not in seen and
                    heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, seen)

        pacific = set()
        atlantic = set()

        for r in range(m):
            dfs(r, 0, pacific)
            dfs(r, n - 1, atlantic)

        for c in range(n):
            dfs(0, c, pacific)
            dfs(m - 1, c, atlantic)

        return list(pacific & atlantic)
