class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        def backtrack(path,used):
            if len(path)==len(nums):
                ans.append(path.copy())
                return 
            for i in range(len(nums)):
                if used[i]:
                    continue 
                used[i]=True
                path.append(nums[i])
                backtrack(path,used)
                path.pop()
                used[i]=False
        backtrack([],[False]*len(nums))
        return ans
