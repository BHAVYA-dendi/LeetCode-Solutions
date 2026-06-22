class Solution(object):
    def twoSum(self, List, target):
        seen={}
        for i,num in enumerate(List):
            c=target-num
            if c in seen:
                return [seen[c],i]
            seen[num]=i  
        


        
