class Solution:
    def maxDistance(self, position, m):
        position.sort()

        def canPlace(dist):
            count = 1
            last = position[0]

            for x in position[1:]:
                if x - last >= dist:
                    count += 1
                    last = x

                    if count == m:
                        return True

            return False

        l, r = 1, position[-1] - position[0]

        while l < r:
            mid = (l + r + 1) // 2

            if canPlace(mid):
                l = mid
            else:
                r = mid - 1

        return l
