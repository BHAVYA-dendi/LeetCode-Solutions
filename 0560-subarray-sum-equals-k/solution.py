class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count={0:1}
        s=0
        ans=0
        for x in nums:
            s+=x
            if s-k in count:
                ans+=count[s-k]
            count[s]=count.get(s,0)+1
        return ans

        
