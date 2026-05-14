class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int prod = 1;
        vector<int> rtnums;
        vector<int> zeroes;
        for(int i=0 ; i < nums.size() ; i++ ){
            if (nums.at(i)!=0){
                prod *= nums.at(i);
            }
            else{
                zeroes.push_back(i);
            }
            
        }
        for(int j=0 ; j < nums.size() ; j++ ){
            if (zeroes.size()==0){
                rtnums.push_back(prod/nums.at(j));
                }
            else if(zeroes.size()==1){
                if(j == zeroes.at(0)){
                    rtnums.push_back(prod);
                }
                else{
                    rtnums.push_back(0);
                }}
            else {rtnums.push_back(0);}
        }
        return rtnums;
    }
};
