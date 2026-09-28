class Solution:
    def rob(self, nums: list[int]) -> int:
        p2=p1=0
        for x in nums:
            p2,p1=p1,max(p1,p2+x)
        return p1
        
