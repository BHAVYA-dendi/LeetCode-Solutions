class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        def backtrack(i,path):
            if i ==len(nums):
                ans.append(path.copy())
                return 
            backtrack(i+1,path)
            path.append(nums[i])
            backtrack(i+1,path)
            path.pop()
        backtrack(0,[])
        return ans
