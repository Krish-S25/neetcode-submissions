class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min = prices[0];
        int max_prof = -1;
        for(int i = 1 ; i<prices.size(); i++){
            if (prices[i]<min){
                min = prices[i];
                continue;
            }
            int profit = prices[i] - min;
            if(profit > 0){
                if (profit > max_prof){
                    max_prof = profit;
                }
            }
        }
        if (max_prof<=0){return 0;}
        return max_prof;
    }
};
