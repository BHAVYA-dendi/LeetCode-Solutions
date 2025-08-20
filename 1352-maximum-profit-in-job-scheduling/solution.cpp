class Solution {
public:
    int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) {
        int n = startTime.size();
        vector<array<int,3>> jobs(n);
        for (int i = 0; i < n; i++) jobs[i] = {endTime[i], startTime[i], profit[i]};
        sort(jobs.begin(), jobs.end());

        vector<int> ends;
        ends.reserve(n);
        for (auto &j : jobs) ends.push_back(j[0]);

        vector<int> dp(n + 1, 0);
        for (int i = 0; i < n; i++) {
            // Option 1: skip this job
            dp[i + 1] = max(dp[i + 1], dp[i]);

            // Option 2: take this job
            int idx = upper_bound(ends.begin(), ends.end(), jobs[i][1]) - ends.begin();
            dp[i + 1] = max(dp[i + 1], dp[idx] + jobs[i][2]);
        }
        return dp[n];
    }
};
