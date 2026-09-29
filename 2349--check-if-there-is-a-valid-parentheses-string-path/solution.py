class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m,n=len(grid),len(grid[0])
        if grid[0][0]==')' or  grid[-1][-1]=='(':
            return False 
        @lru_cache(None)
        def dfs(r,c,bal):
            if bal<0 or bal>m+n:
                return False
            if r==m-1 and c==n-1:
                return bal==0
            for dr,dc in [(1,0),(0,1)]:
                nr,nc=r+dr,c+dc
                if 0<=nr<m and 0<=nc<n:
                    nb=bal+(1 if grid[nr][nc]=='(' else -1)
                    if dfs(nr,nc,nb):
                        return True 
            return False 
        return dfs(0,0,1)
