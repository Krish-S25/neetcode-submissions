class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int curr_sum = nums[0];
        int max_sum = nums[0];
        int n;
        for(int j = 1 ; j<nums.size(); j++ ){
            n = nums[j];

            curr_sum = max(n, curr_sum + n);
            max_sum = max(curr_sum, max_sum);
        }
        return max_sum;
    }
};
