class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
      
      j=1
      max=0
      l=-1
      r=0
      minv=float("inf")
      while j<len(nums):
          
          
          if nums[j]<nums[max]:
              minv=min(minv,nums[j])                                         
              r=j
          if nums[j]>nums[max]:
              max=j
          j+=1
      for i in range(len(nums)):
          if nums[i]>minv:
              l=i
              break
      if l==-1:
          return 0   
      return r-l+1       
           
              
              
              
            
