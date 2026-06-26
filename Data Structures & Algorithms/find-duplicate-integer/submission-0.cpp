class Solution {
public:
    int findDuplicate(vector<int>& nums) {

        int n = nums.size();

        for(int r = 0; r < n; r++){

            int idx = abs(nums[r]);

            if(nums[idx] < 0){
                return idx;
            }
            nums[idx] *= -1;
        }
        return -1;
    }
};