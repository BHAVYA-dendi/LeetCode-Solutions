class Solution:
    def sumSubarrayMins(self, arr):
        MOD = 10**9 + 7
        stack = []
        ans = 0

        for i in range(len(arr) + 1):
            cur = arr[i] if i < len(arr) else 0

            while stack and arr[stack[-1]] > cur:
                j = stack.pop()

                left = j - (stack[-1] if stack else -1)
                right = i - j

                ans += arr[j] * left * right

            stack.append(i)

        return ans % MOD
