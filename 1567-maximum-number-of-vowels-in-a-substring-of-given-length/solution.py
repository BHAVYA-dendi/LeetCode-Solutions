class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels="aeiou"
        v=0
        for i in range(k):
            if s[i] in vowels:
                v+=1
        vmax=v
        i=0
        while i<len(s)-k:
            if s[i] in vowels:
                v-=1
            if s[i+k] in vowels:
                v+=1
            vmax=max(vmax,v)
            i+=1
        return vmax
                    
                
        
