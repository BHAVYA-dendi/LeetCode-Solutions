class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        sol=[]
        nums.sort()
        for a in range(0,len(nums)-3):
            if a>0 and nums[a]==nums[a-1]:
                continue 
            for b in range(a+1,len(nums)-2):
                if b>a+1 and nums[b]==nums[b-1]:
                    continue 
                s=target-nums[a]-nums[b]
                c=b+1
                d=len(nums)-1
                while c<d:
                    if nums[c]+nums[d]<s:
                        u=nums[c]
                        while c<d and nums[c]==u :
                            c+=1
                    elif nums[c]+nums[d]>s:
                        v=nums[d]
                        while c<d and nums[d]==v:
                            d-=1
                        
                    else:
                        t=[nums[a],nums[b],nums[c],nums[d]]
                        
                        sol.append(t)
                        
                        u=nums[c]
                        while c<d and nums[c]==u:
                            c+=1
                        v=nums[d]
                        while c<d and nums[d]==v:
                            d-=1
        return sol          
