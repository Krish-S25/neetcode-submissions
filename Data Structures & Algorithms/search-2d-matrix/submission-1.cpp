#include <algorithm>
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        int n = matrix[0].size();
        int top = 0 , bot = m-1 , row = -1;
        while(top<=bot){
            int mid = top + (bot - top)/2;
            if(matrix[mid][0] == target){
                return true;
            }
            else  if (matrix[mid][0]<target){
                row = mid ;     //just to update if we have the correct row 
                top = mid +1; //standard right case
            }
            else
                bot = mid -1; //standard left case 
        }
        if (row == -1){return false;} //when target < matrix[0][0]
    
        return std::binary_search(matrix[row].begin() , matrix[row].end() , target);
    
    }
};
