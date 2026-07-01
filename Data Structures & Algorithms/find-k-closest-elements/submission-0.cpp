class Solution {
public:    //Method 1 : Binary search
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int n = arr.size();
        int pos = lower_bound(arr.begin(), arr.end(), x) - arr.begin();
        int L = pos-1;
        int R = pos;

        while(k--){
            if(L < 0 ){   //When left is out of bounds
                R++;        
            }
            else if(R > n-1 ){  //When right i sout of bounds
                L--;
            }
            else if(abs(arr[L] - x) <= abs(arr[R] - x)){  //Left closer
                L--; 
            }
            else{                                        //Right closer
                R++;
            }
        }
        return vector<int>(arr.begin()+L+1 , arr.begin()+R);
    }
};