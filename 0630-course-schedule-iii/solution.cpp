class Solution {
public:
    int scheduleCourse(vector<vector<int>>& courses) {
        ios::sync_with_stdio(false);
        cin.tie(NULL);

        sort(courses.begin(), courses.end(),
             [](const vector<int>& a, const vector<int>& b) {
                 return a[1] < b[1];
             });

        priority_queue<int> maxHeap;
        int time = 0;
        for (const auto& c : courses) {
            time += c[0];
            maxHeap.push(c[0]);
            if (time > c[1]) {
                time -= maxHeap.top();
                maxHeap.pop();
            }
        }
        return maxHeap.size();
    }
};
