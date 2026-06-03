class Solution {
public:
    bool checkInclusion(string s1, string s2) {

        if (s2.size() < s1.size()) {
            return false;
        }

        int given[26] = {0};

        for (int r = 0; r < s1.size(); r++) {
            given[s1[r] - 'a']++;
        }

        int getting[26] = {0};

        int L = 0, R = 0;

        getting[s2[0] - 'a']++;  

        while (L <= R && R < s2.size()) {

            if (R - L + 1 < s1.size()) {

                R++;

                if (R < s2.size()) {
                    getting[s2[R] - 'a']++;
                }

            }
            else {

                bool checker = true;

                for (int i = 0; i < 26; i++) {
                    if (getting[i] != given[i]) {
                        checker = false;
                        break;
                    }
                }

                if (checker) {
                    return true;
                }

                getting[s2[L] - 'a']--;
                L++;

                R++;

                if (R < s2.size()) {
                    getting[s2[R] - 'a']++;
                }
            }
        }

        return false;
    }
};