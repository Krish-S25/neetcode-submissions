class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int p1 = 0 ;
        std::string newst;
        int length1 = word1.length();
        int length2 = word2.length();
        while (p1<length1 && p1<length2){
            newst.push_back(word1[p1]);
            newst.push_back(word2[p1]);
            p1+=1 ;
        }
        while(p1<length1){
            newst.push_back(word1[p1]);
            p1++;
        }
        while(p1<length2){
            newst.push_back(word2[p1]);
            p1++;
        }
        return newst ;
        
    }
};