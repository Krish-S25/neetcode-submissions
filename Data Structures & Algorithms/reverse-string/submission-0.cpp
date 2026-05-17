class Solution {
public:
    void reverseString(vector<char>& s) {
        int len = s.size();
        int l = 0 ;
        int r = len-1;

        while(l<r){
            char temp = s[r];
            s[r] = s[l];
            s[l] = temp;
            l++;
            r--;
        }
    }
};