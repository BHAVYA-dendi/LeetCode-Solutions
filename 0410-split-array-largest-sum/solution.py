class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        l=max(nums)
        r=sum(nums)
        while l<r:
            mid=(l+r)//2
            parts=1
            total=0
            for x in nums:
                if total+x>mid:
                    parts+=1
                    total=0
                    
                total+=x
            if parts<=k:
                r=mid
            else:
                l=mid+1
        return l
                
