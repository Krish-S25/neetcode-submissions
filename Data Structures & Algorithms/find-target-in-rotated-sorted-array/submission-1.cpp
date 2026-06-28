class Solution {
public:
    int search(vector<int> &nums, int target) {
        int l = 0;
        int r = nums.size()-1;
        int mid = 0;
        while(l <= r){     
            mid = l + (r-l)/2;
            if(nums[mid] == target){
                return mid;             //Matched
            }
            if(nums[l] <= nums[mid]){    //Check if sorted part on LEFT side
                if(target >= nums[l] && target < nums[mid]){
                    r = mid - 1;                   //Determine if TARGET to LEFT side
                }
                else {l = mid + 1;}                //LEFT side
            }
            else {                       //Check if sorted part on RIGHT side
                if(target > nums[mid] && target <= nums[r]){
                    l = mid + 1;                   //Determine if TARGET to RIGHT side       
                }
                else {r = mid - 1;}                //RIGHT side
            }
        }
        return -1;
    }
};
