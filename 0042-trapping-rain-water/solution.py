class Solution:
    def trap(self, height: List[int]) -> int:
       l=0
       r=len(height)-1
       lmax=height[0]
       rmax=height[len(height)-1]
       w=0
       while l<r:
           if height[l]<height[r]:
               if height[l]>lmax:
                   lmax=height[l]
               else:
                   w+=lmax-height[l]
                   
                   
               l+=1
           else:
               if height[r]>rmax:
                   rmax=height[r]
               else:
                   w+=rmax-height[r]
                   
                   
               r-=1
               
       return w                   
            
           
