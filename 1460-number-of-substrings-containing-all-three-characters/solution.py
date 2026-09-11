class Solution:
    def numberOfSubstrings(self, s: str) -> int:
       last=[-1,-1,-1]
       ans=0
       for r in range(len(s)):
           last[ord(s[r])-ord('a')]=r
           if min(last)!=-1:
               ans+=min(last)+1
               
       return ans   
               
               
         
               
