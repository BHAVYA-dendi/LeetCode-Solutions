class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        while l<r:
            cap=(l+r)//2
            used=1
            current =0
            for w in weights:
                if current+w>cap:
                    used+=1
                    current =0
                current+=w
            if used<=days:
                r=cap
            else:
                l=cap+1
        return l
