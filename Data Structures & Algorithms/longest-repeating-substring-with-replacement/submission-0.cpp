class Solution {
public:
    int characterReplacement(string s, int k) {
        int longest = 0;
        int l = 0 ;
        int cnt[26] = {0};
        for(int r = 0 ; r<s.size() ; r++){
            cnt[s[r] - 'A']++;
            while((r-l+1) - *max_element(cnt, cnt+26) > k){
                cnt[s[l] - 'A']--;
                l++;
            }
            longest = max(longest , r-l+1);
        }   
        return longest;
     }
};
