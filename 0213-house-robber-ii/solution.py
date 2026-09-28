class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(arr):
            prev2 = prev1 = 0
            for x in arr:
                prev2, prev1 = prev1, max(prev1, prev2 + x)
            return prev1

        return max(helper(nums[:-1]), helper(nums[1:]))
        
