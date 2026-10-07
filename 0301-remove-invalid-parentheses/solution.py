class Solution:
    def removeInvalidParentheses(self, s):
        ans = set()

        def dfs(i, path, bal, l, r):
            if bal < 0: return
            if i == len(s):
                if bal == 0 and l == r == 0:
                    ans.add("".join(path))
                return

            if s[i] == '(':
                if l: dfs(i+1, path, bal, l-1, r)
                path.append('(')
                dfs(i+1, path, bal+1, l, r)
                path.pop()

            elif s[i] == ')':
                if r: dfs(i+1, path, bal, l, r-1)
                if bal:
                    path.append(')')
                    dfs(i+1, path, bal-1, l, r)
                    path.pop()

            else:
                path.append(s[i])
                dfs(i+1, path, bal, l, r)
                path.pop()

        l = r = 0
        for c in s:
            if c == '(':
                l += 1
            elif c == ')':
                if l: l -= 1
                else: r += 1

        dfs(0, [], 0, l, r)
        return list(ans)
