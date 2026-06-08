class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int count = 0;
        int check = 0;
        for(int x : nums){
            if(count==0){
                check = x;
            }
            if(x == check){
                count++;
            }
            else{
                count--;
            }
        }
        return check;
    }
};