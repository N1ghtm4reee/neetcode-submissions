class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = position.size();
        if (n == 0) return 0;

        unordered_map<int, int> speeds;
        for (int i = 0; i < n; i++) {
            speeds[position[i]] = speed[i];
        }

        sort(position.begin(), position.end(), greater<int>());

        stack<double> arrivalTimes;

        for (int pos : position) {
            double time = (double)(target - pos) / speeds[pos];
            if (arrivalTimes.empty() || time > arrivalTimes.top())
                arrivalTimes.push(time);
        }

        return arrivalTimes.size();
    }
};
