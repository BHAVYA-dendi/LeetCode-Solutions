class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s=0
        for f in range(1,len(nums)):
            if nums[s]==nums[f]:
                f+=1
                continue
            nums[s+1]=nums[f]  
            f+=1
            s+=1
        return s+1    
        
