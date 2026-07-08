
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
     if len(s)!=len(t):
         return False 
     freq=Counter(s)  
     freq1=Counter(t)
     for c in freq:
         if freq[c]!=freq1[c]:
             return False 
     return True        
