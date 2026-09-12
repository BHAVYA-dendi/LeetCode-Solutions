class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            if target <=nums[l]:
                return l
                
            elif target>nums[r]:
                return r+1
            elif target==nums[r]:
                return r
            else:
                m=(l+r)//2
                if target==nums[m]:
                    return m
                elif target<nums[m]:
                    if l==m-1:
                        return m
                    r=m-1
                else:
                    if r==m+1:
                        return r
                    l=m+1
                        
            
            
