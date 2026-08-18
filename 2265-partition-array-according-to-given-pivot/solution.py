class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less=[]
        great=[]
        equal=[]
        for i in range(0,len(nums)):
            if nums[i]<pivot:
                less.append(nums[i])
            elif nums[i]>pivot:
                great.append(nums[i])
            else:
                equal.append(nums[i])
        return  less + equal +great             
        
