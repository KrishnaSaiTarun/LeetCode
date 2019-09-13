class Solution {
public:
    int minimumTotal(vector<vector<int>>& t) {
        int row = t.size();
        if(row == 0) return 0;
        if(row == 1) return t[0][0];
        
        for(int i= row - 2; i>-1; i--){
            for(int j = 0; j<= i; j++){
                t[i][j] += min(t[i+1][j], t[i+1][j+1]);
            }
        }
        
        return t[0][0]; 
    }
};
