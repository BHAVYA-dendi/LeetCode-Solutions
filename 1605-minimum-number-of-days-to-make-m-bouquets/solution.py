class Solution:
    def minDays(self, bloomDay, m, k):
        if m * k > len(bloomDay):
            return -1

        def canMake(day):
            bouquets = flowers = 0

            for x in bloomDay:
                if x <= day:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0

            return bouquets >= m

        l, r = min(bloomDay), max(bloomDay)

        while l < r:
            mid = (l + r) // 2

            if canMake(mid):
                r = mid
            else:
                l = mid + 1

        return l
