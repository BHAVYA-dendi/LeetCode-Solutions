class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        count={}
        maxfreq=0
        ans=0
        for r in range(len(s)):
            count[s[r]]=count.get(s[r],0)+1
            maxfreq=max(maxfreq,count[s[r]])
            while (r-l+1)-maxfreq>k:
                count[s[l]]-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans
            
        
