class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def find(first):
            l=0
            r=len(nums)-1
            ans=-1

            while l <= r:
                m = (l + r) // 2

                if nums[m] == target:
                    ans = m

                    if first:
                        r = m - 1
                    else:
                        l = m + 1

                elif nums[m] < target:
                    l = m + 1

                else:
                    r = m - 1

            return ans

        return [find(True), find(False)]
        
