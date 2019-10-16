class Solution {
public:
    int isSymbol_number(char a){
        
        if(a == '-')
            return -1;
        if(a == '+')
            return 1;
        if(a >= '0' && a<= '9')
            return 2;
        
        else return 3;
    }
    int myAtoi(string str) {
        
        long int ret = 0;
        int i = 0;
        while(str[i]==' ') i++;

        int sign = isSymbol_number(str[i]);
        switch(sign){

            case 3: return 0;
            case 2: sign = 1;
                break;
            default: i++;
            break;
        }
        
        while(str[i] != '/0' && str[i]>= '0' && str[i]<= '9' ){
            
            ret = ret*10 + (str[i] - '0'); 
            i++;
            
            if(ret >= INT_MAX)
                return sign == -1? INT_MIN:INT_MAX;
        }
        
        return sign*ret;
        
    }
};
