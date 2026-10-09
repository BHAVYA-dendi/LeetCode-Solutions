class Solution:
    def minInsertions(self, s: str) -> int:
        ans=bal=0
        for ch in s:
            if ch=='(':
                if bal%2:
                    ans+=1
                    bal-=1
                bal+=2
            else:
                bal-=1
                if bal<0:
                    ans+=1
                    bal=1
                    
        return ans+bal
