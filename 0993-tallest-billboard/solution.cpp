class Solution {
public:
    int tallestBillboard(vector<int>& rods) {
        int sum = accumulate(rods.begin(), rods.end(), 0);
        vector<int> dp(2 * sum + 1, -1);
        dp[sum] = 0;

        for (int r : rods) {
            auto cur = dp;
            for (int d = 0; d <= 2 * sum; d++) {
                if (cur[d] < 0) continue;
                dp[d + r] = max(dp[d + r], cur[d]);
                dp[d - r] = max(dp[d - r], cur[d] + r);
            }
        }
        return dp[sum];
    }
};
