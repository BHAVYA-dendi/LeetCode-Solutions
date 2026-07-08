class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana={}
        for s in strs:
            freq=[0]*26
            for c in s:
              i=ord(c)-ord('a')
              freq[i]+=1
            st=tuple(freq)
            if st in ana:
                
                ana[st].append(s)
                
                
            else:
               ana[st]=[s]  
        return [ana[f] for f in ana]    
