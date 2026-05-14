#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    string encode(vector<string>& strs) {
        string fin = "";
        for(const string& s: strs) {
            fin += to_string(s.length()) +"^"+ s;
        }
        return fin;
    }

    vector<string> decode(string s) {
        vector<string> decoded_strs;
        int i = 0;
        
        while (i < s.length()) {
            int j = i;
            while (s[j] != '^') {
                j++;
            }    
            int length = stoi(s.substr(i, j - i));
            string str = s.substr(j + 1, length);
            decoded_strs.push_back(str);
            i = j + 1 + length;
        }
        return decoded_strs;
    }
};