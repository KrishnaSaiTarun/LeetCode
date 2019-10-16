class Solution {
public:
    int numMagicSquaresInside(vector<vector<int>>& grid) {
        
        int row = grid.size();
        if(row<3) return 0;
        int col = grid[0].size();
        if(col<3) return 0;
        int count = 0;
        for(int i = 0; i< row-2; i++){
            
            for(int j = 0; j< col-2; j++){
                
                if(grid[i+1][j+1]!=5) continue;
                
                if(are_distinct(grid, i, j) && row_sum(grid,i,j) && col_sum(grid,i,j) && diag_sum(grid,i,j)) count++;
            }
        }
        
        return count;
        
    }
    
    bool are_distinct(vector<vector<int>>& grid, int i, int j){
        
        vector<int> check(9,0);
        for(int k = i; k<i+3; k++){
            
            for(int t = j; t< j+3; t++){
                
                if(grid[k][t]>9 || grid[k][t]<=0) return false;
                
                check[grid[k][t]-1] += 1;
                if(check[grid[k][t]-1] == 2) return false;
        
            }
     
            
        }
        
        
        return true;
    }
    
    bool row_sum(vector<vector<int>>& grid, int i, int j){
        int sum = 0;
        for(int k=i; k<i+3; k++){
            for(int t=j;t<j+3;t++){
                sum+=grid[k][t];
            }
            if(sum!=15) return false;
            else sum = 0;
        }
        return true;
    } 
    
    
    bool col_sum(vector<vector<int>>& grid, int i, int j){
        int sum = 0;
        for(int k=j; k<j+3; k++){
            for(int t=i;t<i+3;t++){
                sum+=grid[t][k];
            }
            if(sum!=15) return false;
            else sum = 0;
        }
        return true;
    }
    
    
    bool diag_sum(vector<vector<int>>& grid, int i, int j){
        int sum = 0;
        for(int k=j, t=i; k<j+3, t<i+3; k++, t++){
         
                sum+=grid[t][k];
            }
            if(sum!=15) return false;
            else sum = 0;
            
            for(int k=j+2, t=i; k>=j, t<i+3; k--, t++){
         
                sum+=grid[t][k];
            }
            if(sum!=15) return false;
            else sum = 0;
                
                return true;
                
        }
        
};
