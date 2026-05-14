class Solution {
public:
    bool isAnagram(string s, string t) {
        int ct1[26] ={0};
        int ct2[26] ={0};
        if(t.length()!= s.length()) return false;
        for(int i = 0 ; i<t.length() ; i++ ){
            int cs = s[i] -'a';
            int ct = t[i]-'a';
            ct1[cs]++;
            ct2[ct]++;
        }
        for (int i = 0; i < 26; i++) {
        if (ct1[i] != ct2[i])
        return false;
                }
        return true;
    }
};
