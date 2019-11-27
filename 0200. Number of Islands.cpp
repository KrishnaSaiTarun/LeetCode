class Solution {
public:
    
    void dfs(int i, int j, int row, int col, vector<vector<char>>& grid){
        
        grid[i][j] = '0';
        
        if(i + 1 < row && grid[i+1][j] == '1') dfs(i+1, j, row, col, grid);
        if(i - 1 >= 0 && grid[i-1][j] == '1') dfs(i-1, j, row, col, grid);
        if(j - 1 >= 0 && grid[i][j-1] == '1') dfs(i, j-1, row, col, grid);
        if(j + 1 < col && grid[i][j+1] == '1') dfs(i, j+1, row, col, grid);
    }
    
    int numIslands(vector<vector<char>>& grid) {
        
        int row = grid.size();
        if(!row) return 0;
        int col = grid[0].size();
        int islands = 0;
        
        for(int i = 0; i < row; i++){
            
            for(int j=0; j < col; j++){
                
                if(grid[i][j] == '1'){
                    
                    islands+=1;
                    dfs(i, j, row, col, grid);
                    
                }
                
            }
        }
        
        return islands;
        
    }
};
