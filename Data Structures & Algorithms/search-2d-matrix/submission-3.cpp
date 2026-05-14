#include <algorithm>

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        int n = matrix[0].size();
        int top = 0 , bot = m-1 , row = -1;
        while(top<=bot){
            int mid = top + (bot-top)/2;
            if(target==matrix[mid][0]){
                return true;
            }
            else if(target>matrix[mid][0]){
                row = mid;
                top = mid+1;
            }
            else{
                bot = mid-1;
            }
            }
            if(row == -1){
                return false;
            }
            return std::binary_search(matrix[row].begin() ,matrix[row].end() , target );
    }
};
