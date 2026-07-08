class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        s=len(nums)
        prefix=[1]*s
        suffix=[1]*s
        for i in range(0,s):
            if i!=0:
                prefix[i]=prefix[i-1]*nums[i-1]
            
                suffix[s-1-i]=suffix[s-i]*nums[s-i]
                
        return list(prefix[i]*suffix[i] for i in range(0,s))
        
           
        
