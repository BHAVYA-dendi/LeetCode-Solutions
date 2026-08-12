class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=0
        r=len(nums)-1
        res=[0]*len(nums)
        i=len(nums)-1
        while l<=r:
            ls=nums[l]*nums[l]
            rs=nums[r]*nums[r]
            if ls<rs:
                res[i]=rs
                i-=1
                r-=1
            else:
                res[i]=ls
                i-=1
                l+=1
        return res
                
                
