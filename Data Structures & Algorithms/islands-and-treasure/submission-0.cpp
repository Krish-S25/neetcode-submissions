class Solution {
public:        //Not correct , WE SHOULD USE BFS instead of DFS
    void islandsAndTreasure(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        queue<pair<int,int>> Q;
        for(int i = 0 ; i < m ; i++){
            for(int j = 0 ; j < n ; j++){
                if(grid[i][j] == 0){
                    Q.push({i,j});
                }
            }
        }
        vector<pair<int,int>> dx_dy = { {-1,0}, {1,0}, {0,-1}, {0,1} };
        const int inf = 2147483647;
        while (!Q.empty()){
            auto [r,c] = Q.front();
            Q.pop();

            for(auto [dx , dy] : dx_dy){
                int newX = dx + r;
                int newY = dy + c;
                if((newX<0)||(newX>=m)||(newY<0)||(newY>=n)||
                (grid[newX][newY]!= inf)){ continue; }

                grid[newX][newY] = grid[r][c] + 1;
                Q.push({newX,newY});
            }

        }

    }
};
