class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        s=0
        for a in range(len(nums)-1,1,-1):
            if nums[a-2] + nums[a-1] <= nums[a]:
                continue
                
    
            b=0
            c=a-1
            while b<c:
                if nums[b]+nums[c]>nums[a]:
                    s+=c-b
                    c-=1
                else:
                    b+=1
                    
           
        return s      
                        
            
