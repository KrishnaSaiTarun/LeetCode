class Solution {
public:
    int romanToInt(string s) {
        
        int i = s.length() - 1; 
        int sum = 0;
        
        while(i>-1){
            char a = s[i];
            switch(a){
                
                case 'I': sum+= 1;
                break;
                case 'V': if(i-1> -1 && s[i-1] == 'I') {sum+=4; i--;}
                else sum+= 5;
                
                break;
                case 'X': if(i-1> -1 && s[i-1] == 'I') {sum+=9; i--;}
                else sum+= 10;
                break;
                case 'L': if(i-1> -1 && s[i-1] == 'X') {sum+=40; i--;}
                else sum+= 50;
                break;
                case 'C': if(i-1> -1 && s[i-1] == 'X') {sum+=90; i--;}
                else sum+= 100;
                break;
                case 'D': if(i-1> -1 && s[i-1] == 'C') {sum+=400; i--;}
                else sum+= 500;
                break;
                case 'M': if(i-1> -1 && s[i-1] == 'C') {sum+=900; i--;}
                else sum+= 1000;
                break;
                
            }
            
            i--;
        }
        
        return sum;
        
    }
};
