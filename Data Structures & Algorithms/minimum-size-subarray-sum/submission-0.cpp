class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int l = 0;
        int sm = 0;
        int ans = INT_MAX;

        for(int r = 0 ; r < nums.size() ; r++){
            sm += nums[r];
            while(sm>=target){
                ans = min(ans , r - l + 1);
                sm-= nums[l];
                l++;
            }   
        }
        
        if(ans == INT_MAX){ return 0; }

        else{ return ans; }
    }
};