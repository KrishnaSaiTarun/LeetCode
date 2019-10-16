class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.length();
        if(n==0 || n==1) return s;
        vector<vector<int>> b(n,vector<int>(n,0));
        int start = 0;
        int len = 1;
        for(int i = 0; i < n; i++){
            b[i][i] = 1;
        }
        for(int i=0; i< n-1; i++){
            if(s[i]==s[i+1]){
                b[i][i+1] = 1;
                start = i;
                len = 2;
            }
        }     
        for(int l = 3; l <= n; l++){
                int j= l-1;
            for(int i = 0; i<n-j; i++){
                
                if(s[i] == s[i+j] && b[i+1][i+j-1]){
                    
                 b[i][i+j] = 1;
                 start = i;
                 len = l;   
                }
            }
        }
        
        return s.substr(start,len);
        
        
    }
};
