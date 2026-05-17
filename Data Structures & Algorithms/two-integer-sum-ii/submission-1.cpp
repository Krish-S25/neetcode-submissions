class Solution {
public:
    int binarysearch(vector<int>& numbers, int diff , int l , int r){
        while(l<=r){
            int mid = l + (r-l)/2;
            if (numbers.at(mid) == diff){ return mid; }
            else if (numbers.at(mid)<diff) {
                l = mid + 1;
            }
            else{
                r = mid - 1;
            }
        }
        return -1;
    }

    vector<int> twoSum(vector<int>& numbers, int target) {
        int length = numbers.size();
        for(int i = 0 ; i < length ; i++){
            int diff = target - numbers[i];
            
            // FIXED: Start at i + 1 to avoid duplicates, end at length - 1 to avoid crashes
            int comp = binarysearch(numbers, diff , i + 1 , length - 1);
            
            if(comp!=-1){
                vector<int> temp = {i+1 , comp+1};
                return temp;
            }
        }
        vector<int> temp ;
        return temp;
    }
};