class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp=list(range(len(word2)+1))
        for i,a in enumerate(word1,1):
            prev=dp[0]
            dp[0]=i
            for j,b in enumerate(word2,1):
                temp=dp[j]
                if a==b:
                    dp[j]=prev
                else:
                    dp[j]=1+min(dp[j],dp[j-1],prev)
                prev=temp
        return dp[-1]
                
           
