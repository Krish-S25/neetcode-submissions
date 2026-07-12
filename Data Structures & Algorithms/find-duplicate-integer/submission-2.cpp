class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int slow = 0;
        int fast = 0; 
        do{            //checking for cycle formation
            slow= nums[slow];         
            fast= nums[nums[fast]]; } 
            while(slow!=fast); //both slow and fast are part of cycle when repeated
        
        slow = 0;         //now finding the repeated number in cycle
        while(slow!=fast){
            slow = nums[slow];
            fast = nums[fast];
        }
        return fast; //or slow

    }
};