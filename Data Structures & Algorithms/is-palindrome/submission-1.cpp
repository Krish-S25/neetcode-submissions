#include <string>
#include <cctype>
class Solution {
public:
    bool isPalindrome(string s) {
        int i = 0 , j = s.length() - 1 ;
        while(i < j ){
            unsigned char left = static_cast<unsigned char>(s[i]);
            unsigned char right = static_cast<unsigned char>(s[j]);
            if(!isalnum(left)){
                i++;
                continue;
            }
            if(!isalnum(right)){
                j--;
                continue;
            }
            if(std::tolower(left) != std::tolower(right)){return false;}
            i++;
            j--;
        }
        return true;
    }
};
