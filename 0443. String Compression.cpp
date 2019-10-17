class Solution {
public:
    int compress(vector<char>& chars) {
 
        int left = 0;
        int right = 0, len = chars.size();
        if(len == 0 || len == 1) return len;
        int count = 1;
        for(int i=1; i<chars.size(); i++){
            
            
            if(chars[i-1] == chars[i]) {
                count++; 
            }
            
            else{
                
                if(count == 1){
                    chars[++left] = chars[i];
                }
                else{
                    
                    string num = to_string(count);
                    
                    for(char c: num)  
                        chars[++left] = c;
                    
                    chars[++left] = chars[i];
                    count = 1;
                }
            }
            
        }
        
        if(count > 1){
            
            string num = to_string(count);
                    
                    for(char c: num)  
                    chars[++left] = c;
            
        }
        
        return left+1;
        
    }
};
