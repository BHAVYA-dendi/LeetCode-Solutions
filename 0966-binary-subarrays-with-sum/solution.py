class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atmost(k):
            if k<0:
                return 0
            l=0
            s=0
            ans=0
            
            for r in range(len(nums)):
                s+=nums[r]
                while s>k:
                    s-=nums[l]
                    l+=1
                ans+=r-l+1
            return ans
        return atmost(goal)-atmost(goal-1)
            
        
