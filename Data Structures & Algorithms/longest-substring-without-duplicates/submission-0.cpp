class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char,int> lastind;
        int left = 0;
        int maxlen = 0;
        for(int right = 0; right<s.length();right++){
            if (lastind.count(s[right])){
                left = max(left , lastind[s[right]]+1);
            }
            lastind[s[right]]=right;
            maxlen = max(maxlen , right-left+ 1 );
        }
        return maxlen;
    }
};
