class Solution {
public:
    int possible(vector<int>& weights, int days, int capacity){
        int need = 1;
        int load = 0;
        for(int w: weights){
            if(load+w > capacity){
                need++ ;
                load = 0;
            }
            load += w;
        }
        return (need<=days);
    }

    int shipWithinDays(vector<int>& weights, int days) {
        int l = *max_element(weights.begin(), weights.end());
        int r = accumulate(weights.begin(), weights.end(),0);
        int ans = r;
        while(l<=r){
            int mid = (l + r)/2;
            if(possible(weights,days,mid)){
                ans = mid;
                r = mid-1;
            }
            else{
                l=mid+1;
            }
        }
        return ans;
        
    }
};