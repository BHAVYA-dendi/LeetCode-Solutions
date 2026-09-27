class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        n = len(matrix[0])
        heights = [0] * n
        ans = 0

        def histogram(h):
            stack = []
            best = 0
            h = h + [0]

            for i, x in enumerate(h):
                while stack and h[stack[-1]] > x:
                    height = h[stack.pop()]
                    left = stack[-1] if stack else -1
                    width = i - left - 1
                    best = max(best, height * width)

                stack.append(i)

            return best

        for row in matrix:
            for j in range(n):
                if row[j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0

            ans = max(ans, histogram(heights))

        return ans
