class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        l, r = 0, max(diff)

        while l < r:
            mid = (l + r) // 2
            need = sum(max(0, x - mid) for x in diff)

            if need <= k:
                r = mid
            else:
                l = mid + 1

        level = l
        ans = 0
        remaining = k

        for x in diff:
            if x > level:
                remaining -= x - level
                ans += level * level
            else:
                ans += x * x

        # Use remaining operations to reduce values currently at 'level'
        for x in diff:
            if remaining == 0:
                break
            if x >= level and level > 0:
                ans -= level * level - (level - 1) ** 2
                remaining -= 1

        return ans
