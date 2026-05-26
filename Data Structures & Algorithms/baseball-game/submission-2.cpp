#include <vector>
#include <string>
class Solution {
public:
    int calPoints(vector<string>& operations) {
        int cs = 0;
        vector<int> st ; 
        for(const string& k : operations){
            if (k =="+"){
                int t1 , t2 , sm ;
                t2 = st.back();
                st.pop_back();
                t1 = st.back();
                sm = t1+t2;
                st.push_back(t2);
                st.push_back(sm);
            }
            else if (k == "D"){
                int t1 , sm;
                t1 = st.back();
                st.push_back(2*t1);
            }
            else if (k == "C"){
                st.pop_back();
            }
            else{
                st.push_back(stoi(k));
            }
        }
        for (auto i : st) {
            cs += i;
        }

        return accumulate(st.begin(),st.end(),0);
    }
};