class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();
                                         //USE THE ORIGINAL LIST AS HASH MAP
        for(int i = 0; i < n ; i++ ){    //ONLY 1...n numbers matter
            while((nums[i]>=1) && (nums[i]<=n) && nums[i]!=nums[nums[i]-1]){
                swap(nums[i], nums[nums[i]-1]); 
            }              //swap needed until we get matching hash element for index i
        }   
        for(int j = 0; j<n ; j++){
            if(nums[j] != j+1){ return j+1 ; }
        }
        
        return n+1; //when NUMS has only numbers from 1....n
    }
};