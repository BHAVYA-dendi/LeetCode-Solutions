class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        c=2*n
        res={}
        for r,s in reservedSeats:
            
            if r not in res:
                res[r]=set()
            res[r].add(s)   
        for i in res:
            c-=2
            seats=res.get(i,set())
            left=all(x not in seats for x in [2,3,4,5])
            right=all(x not in seats for x in [6,7,8,9])
            if left:
                c+=1
            if right:
                c+=1
            if not left and not right:
                middle=all(x not in seats for x in [4,5,6,7])   
                if middle:
                    c+=1
                    
                           
        return c
        
