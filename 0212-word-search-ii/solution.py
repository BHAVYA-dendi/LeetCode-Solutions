class Solution:
    def findWords(self, board, words):
        root = {}

        for word in words:
            cur = root
            for ch in word:
                cur = cur.setdefault(ch, {})
            cur["#"] = word

        m, n = len(board), len(board[0])
        ans = []

        def dfs(r, c, node):
            ch = board[r][c]

            if ch not in node:
                return

            nxt = node[ch]

            if "#" in nxt:
                ans.append(nxt["#"])
                del nxt["#"]

            board[r][c] = "#"

            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    if board[nr][nc] != "#":
                        dfs(nr, nc, nxt)

            board[r][c] = ch

            if not nxt:
                del node[ch]

        for r in range(m):
            for c in range(n):
                dfs(r, c, root)

        return ans
