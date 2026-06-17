#include <vector>
#include <stack>
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> res(n,0);
        stack<int> sk ;
        for(int i = 0; i<n ; i++){
            while(!sk.empty() && temperatures[i] > temperatures[sk.top()]){
                int prev_day = sk.top();
                sk.pop();
                res[prev_day] = i - prev_day;
            }
            sk.push(i); }
    return res;
    }
};
