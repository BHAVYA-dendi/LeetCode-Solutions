class Solution:
    def smallestDivisor(self, nums, threshold):
        def valid(d):
            total = 0

            for x in nums:
                total += (x + d - 1) // d

            return total <= threshold

        l, r = 1, max(nums)

        while l < r:
            mid = (l + r) // 2

            if valid(mid):
                r = mid
            else:
                l = mid + 1

        return l
