class Solution {
public:
    int removeElement(vector<int>& nums, int val) {

        int sp = 0;
        int ep = nums.size() - 1;
        while (sp <= ep) {
            if (nums[sp] == val) {
                swap(nums[sp],nums[ep]);
                ep--;
            }
            else {
                sp++;
            }
        }
        return sp;
    }
};