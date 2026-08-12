class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        s=0
        for f in range(len(nums)):
            if nums[f]!=0:
                if s!=f:
                    nums[s],nums[f]=nums[f],nums[s]
                s+=1
            
        
