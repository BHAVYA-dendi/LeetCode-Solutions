class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        c={}
        for i in range(len(nums)-k+1):
            s=set(nums[i:i+k])
            for x in s:
                c[x]=c.get(x,0)+1
        maxx=-1
        for x in c:
            if c[x]==1:
                maxx=max(maxx,x)
                
        return maxx       
            
            
                 
        
