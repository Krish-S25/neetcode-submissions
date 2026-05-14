class Solution {
public:
    bool checkanagram(string s , string t){
        if (s.length() != t.length()) return false;

        int cnt[26] = {0};

        for (int i = 0; i < s.length(); i++) {
            cnt[s[i] - 'a']++;
            cnt[t[i] - 'a']--;
        }

        for (int i = 0; i < 26; i++)
            if (cnt[i] != 0) return false;

        return true;
    }
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> final;
        vector<bool> used(strs.size() , false);
        for (int p = 0 ; p < strs.size() ; p++){
            if(used[p]){
                continue;
            }
            vector<string> pst ;
            pst.push_back(strs.at(p));
            used[p]= true;
            for(int q = p+1 ; q<strs.size();q++){
                if(!used[q] && checkanagram(strs.at(p),strs.at(q))){
                    pst.push_back(strs.at(q));
                    used[q] = true;
                }
            }
        final.push_back(pst);
        }
        return final;
    }
};
