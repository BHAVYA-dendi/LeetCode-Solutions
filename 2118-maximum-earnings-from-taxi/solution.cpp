class Solution {
public:
    long long maxTaxiEarnings(int n, vector<vector<int>>& rides) {
        sort(rides.begin(), rides.end(), [](auto &a, auto &b){
            return a[1] < b[1];
        });
        
        int m = rides.size();
        vector<long long> dp(m + 1, 0);
        vector<int> ends;
        for (auto &r : rides) ends.push_back(r[1]);

        for (int i = 0; i < m; i++) {
            dp[i + 1] = max(dp[i + 1], dp[i]); 
            long long earn = (long long)(rides[i][1] - rides[i][0] + rides[i][2]);
            int j = upper_bound(ends.begin(), ends.end(), rides[i][0]) - ends.begin();
            dp[i + 1] = max(dp[i + 1], dp[j] + earn);
        }
        return dp[m];
    }
};
