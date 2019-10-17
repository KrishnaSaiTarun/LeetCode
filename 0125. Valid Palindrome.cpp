class Solution {
public:
    bool isPalindrome(string s) {
        
        int len = s.length();
        if(len == 0) return true;
        
        int l = 0;
        int r = len -1; 
        
        while(l<r){
            
            char c1 = tolower(s[l]);
            if(!((c1>='0' && c1<='9') || (c1>='a' && c1<='z'))){
                
                l++;
                continue;
            }
            
            char c2 = tolower(s[r]);
            if(!((c2>='0' && c2<='9') || (c2>='a' && c2<='z'))){
                
                r--;
                continue;
            }
            
            if(c1 != c2) return false;
            
            else{
                l++; r--;
            }
        }
        
        return true;
        
    }
};
