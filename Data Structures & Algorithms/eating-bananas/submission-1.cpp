#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool isPossible(vector<int>& piles, int h, int rate) {
        long long hours_needed = 0;
        for (int i = 0; i < piles.size(); i++) {
            hours_needed += (piles[i] + rate - 1) / rate;
        }
        return hours_needed <= h;
    }

    int minEatingSpeed(vector<int>& piles, int h) {
        int l = 1; 
        int r = *max_element(piles.begin(), piles.end());
        
        while (l < r) {
            int mid = l + (r - l) / 2;
            
            if (isPossible(piles, h, mid)) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return l;
    }
};

// remaining h>0 -> some hours left -> can lower rate
// remaining h=0 -> no hours left -> possible rate solution,check for rate-1
// remaining h<0 -> need more hours -> need higher rate
