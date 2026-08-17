class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        mincost=0
        s=list(s)
        l=0
        r=len(s)-1
        while l<r:
            if s[l]!=s[r]:
                lcost=0                          
                for j in range(r-1,l-1,-1):
                    lcost+=1
                    if s[j]==s[l]:
                        break
                if j==l:
                    
                    lcost=1    
                    s[j],s[j+1]=s[j+1],s[j] 
                    mincost+=lcost     
                    
                else:
                    for k in range(j,r):
                        s[k],s[k+1]=s[k+1],s[k]
                    mincost+=lcost
                    l+=1
                    r-=1
                       
                        
            else:
                l+=1
                r-=1
        print(s)
        return mincost       
