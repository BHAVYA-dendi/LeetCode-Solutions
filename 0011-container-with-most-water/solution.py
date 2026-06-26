class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        h=len(height)-1
        maxh=0
        while l<h:
            if height[l]<height[h]:
                minh=height[l]
            else:
                minh=height[h]
                    
            if maxh<minh*(h-l):
                maxh=minh*(h-l)
                    
            
            if height[l]<height[h]:
                hp=height[l]
                while hp>=height[l] and l<h:
                    l+=1
                   
            else:
                hph=height[h]
                while hph>=height[h] and l<h:
                    h-=1
      
        return maxh      
