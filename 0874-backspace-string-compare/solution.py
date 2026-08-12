class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i=len(s)-1
        j=len(t)-1
        skip_s=0
        skip_t=0
        while i>=0 or j>=0:
          if i>=0:
            if s[i]=='#':
                skip_s+=1
                i-=1
                continue
            if skip_s>0:
                
                i-=1
                skip_s-=1
                continue
                
          if j>=0:
            if t[j]=='#':
                skip_t+=1
                j-=1
                continue 
            if skip_t>0:
               
                j-=1
                skip_t-=1
                continue 
                    
                
          if i>=0 and j>=0 and s[i]==t[j]:
              i-=1
              j-=1
          else:
              return False
        return True
                    
            
        
