class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack=[]
        greater={}
        for x in nums2:
            while stack and x>stack[-1]:
                greater[stack.pop()]=x
                
            stack.append(x)
        return [greater.get(x,-1) for x in nums1]   
