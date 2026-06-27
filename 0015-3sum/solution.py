class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        sol=[]
        for i,n in enumerate(nums):
            if n>0:
                break
            if i>0 and nums[i-1]==n:
                continue
            value=0-n
             
            l=i+1
            h=len(nums)-1
            while l<h:
               if nums[l]+nums[h]<value:
                   l+=1
                   
               elif nums[l]+nums[h]>value:
                   h-=1
                     
               else:
                   sol.append([n,nums[l],nums[h]])
                   l+=1
                   h-=1
                   while nums[l-1]==nums[l] and l<h:
                      l+=1
                   while nums[h+1]==nums[h] and l<h:
                      h-=1   
                   
        return sol         
                          
            
            
