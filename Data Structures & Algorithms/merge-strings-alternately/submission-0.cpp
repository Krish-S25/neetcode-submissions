class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int p1 = 0 ;
        std::string newst;
        while (p1<word1.length() && p1<word2.length()){
            newst.push_back(word1[p1]);
            newst.push_back(word2[p1]);
            p1+=1 ;
        }
        while(p1<word1.length()){
            newst.push_back(word1[p1]);
            p1++;
        }
        while(p1<word2.length()){
            newst.push_back(word2[p1]);
            p1++;
        }
        return newst ;
        
    }
};