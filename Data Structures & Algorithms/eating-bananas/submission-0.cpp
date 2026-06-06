using namespace std;

class Solution {
public:
    int possible(vector<int>& piles, int h, int rate) {
        if (rate <= 0) return -1; 
        long long remaining_h = h;
        
        for (int i = piles.size() - 1; i >= 0; i--) {
            remaining_h -= (piles[i] + rate - 1) / rate;  
        }
        
        if (remaining_h > 0) { 
            return 1; 
        } else if (remaining_h == 0) { 
            return 0; 
        } else { 
            return -1; 
        }
    }

    int minEatingSpeed(vector<int>& piles, int h) {
        int maxval = *max_element(piles.begin(), piles.end());
        int l = 1, r = maxval;
        
        while (l < r) {
            int mid = l + (r - l) / 2;
            int current_status = possible(piles, h, mid);
            
            if (current_status == 0) {
                int checklower = possible(piles, h, mid - 1);
                if (checklower != 0 && checklower != 1) { 
                    return mid; 
                } else {
                    r = mid - 1;
                }
            } 
            else if (current_status < 0) {
                l = mid + 1;
            } 
            else {
                r = mid;
            }
        }
        return l;
    }
};

// remaining h>0 -> some hours left -> can lower rate
// remaining h=0 -> no hours left -> possible rate solution,check for rate-1
// remaining h<0 -> need more hours -> need higher rate
