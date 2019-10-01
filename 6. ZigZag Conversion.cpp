class Solution {
public:
    string convert(string s, int n) {
        
        bool flag = false;
        if(n == 0) return "";
        if(n == 1) return s;
        int row = 0;
        string str_row[n];
        for(int i=0; i<s.length(); i++){
            str_row[row]+=s[i];
            
            if(row == 0){
                flag = true;
            }
            if(row == n-1) flag = false;
            
            if(flag) row++;
            
            else row--;
            
        }
        
        string ret = "";
        for(int i = 0; i< n; i++){
            ret += str_row[i];
        }
        
        return ret;

        
        
//         int i = 0;
//         string res = "";
//         int len = s.length();
//         if(n == 0) return res;
//         if(n == 1) return s;
//         while(i<n){
            
//                 int k = i;
//                 res = res + s[k];
//                 while(k<len){
//                 int down = (n-1)-i;
//                 k+= (down*2);
//                 if(k<len && down!=0)
//                 res = res + s[k];                
//                 int up = i - 0;
//                 k+= (2*up);
//                 if(k<len && up!=0)            
//                 res = res + s[k];
                
//                 }
//                 i++;
//             }
        
        
//         return res;   
        
        
        
    }
};
