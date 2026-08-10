class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        longest=0
        for n in numset:
            if n-1 not in numset:
                c=n
                l=1
                while c+1 in numset:
                    c+=1
                    l+=1
                    
                longest=max(longest,l)
                
        return longest       
