class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        b=[[] for _ in range(len(nums)+1) ]
        for n,c in freq.items():
            b[c].append(n)
        unique=[]
        for c in range(len(b)-1,0,-1):
            for n in b[c]:
                unique.append(n)
                if len(unique)==k:
                    return unique
        return unique            
