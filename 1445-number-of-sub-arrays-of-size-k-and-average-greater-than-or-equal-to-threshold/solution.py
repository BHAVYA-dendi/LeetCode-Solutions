class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ws=sum(arr[:k])
        avg=ws/k
        avgn=0
        if avg>=threshold:
            avgn+=1
        i=0
        while i<len(arr)-k:
            ws=ws-arr[i]+arr[i+k]  
            avg=ws/k
            if avg>=threshold:
                avgn+=1
            i+=1
            
        return avgn
        
