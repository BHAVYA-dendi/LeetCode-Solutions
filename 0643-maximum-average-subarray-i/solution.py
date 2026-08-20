class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        ws=sum(nums[:k])
        r=ws/k
        i=0
        while i<=len(nums)-k-1:
            ws=ws-nums[i]+nums[i+k]
            r=max(r,ws/k)
            i+=1
        return r
        
