class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans=[]
        def backtrack(start,path,total):
            if total==target:
                ans.append(path.copy())
                return 
            if total>target:
                return 
            for i in range(start,len(candidates)):
                path.append(candidates[i])
                backtrack(i,path,total+candidates[i])
                path.pop()
        backtrack(0,[],0)
        return ans
