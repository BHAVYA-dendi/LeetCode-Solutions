class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        c=0
        l=0
        h=len(people)-1
        people.sort()
        while l<=h:
            if people[l]+people[h]>limit:
                h-=1
               
                c+=1
            else:
                h-=1
                l+=1
                c+=1
        return c
            
