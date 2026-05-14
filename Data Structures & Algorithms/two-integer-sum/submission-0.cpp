class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
            int l =0, r = 1;
            for(int i = 0;i<nums.size()-1;i++){
                int j ;
                int st = target - nums[i];
                for(j = i+1; j<nums.size() ; j++){
                    if(st == nums[j]){
                        r = j;
                        l = i;
                        break;
                    }
                }
            }
            vector<int> res = {l , r};
            return res;
    }
};
