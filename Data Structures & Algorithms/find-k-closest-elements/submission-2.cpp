class Solution {
public:   //Mehtod 2 : Binary search on sliding window
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int l = 0;
        int r = arr.size()-k;

        while(l<r){
            int mid = l+ (r-l)/2;
            //  x-low end    x-high end
            if(x-arr[mid] > arr[mid+k] - x){    //When high end closer
                l = mid + 1; 
            }
            else{                 //When low end closer
                r = mid;
            }
        }
        return vector<int>(arr.begin()+l , arr.begin()+l+k);
    }
};