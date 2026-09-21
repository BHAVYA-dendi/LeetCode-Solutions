class Solution:
    def isHappy(self, n: int) -> bool:
        def nxt(n):
            s=0
            while n:
                s+=(n%10)**2
                n//=10
            return s
        s=n
        f=nxt(n)   
        while f!=1 and s!=f:
            s=nxt(s)
            f=nxt(nxt(f))
        return f==1
