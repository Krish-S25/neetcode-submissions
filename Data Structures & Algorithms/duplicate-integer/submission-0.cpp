class Solution {
public:
    bool hasDuplicate(vector<int>& nums){
    unordered_map<int,bool> seen;
    for (int num : nums) {
        if (seen[num]) 
            return true;
        seen[num] = true;
    }
    return false;
}
    
};