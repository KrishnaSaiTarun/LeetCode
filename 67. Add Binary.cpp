class Solution {
public:
    
    string addBinary(string a, string b) {
        
        int ap = a.length() - 1;
        int bp = b.length() - 1;
        string out = "";
        int ad, bd, carry = 0;
        
        while(ap>=0 || bp>=0 || carry==1){
            
            ad = bd = 0;
            
            if(ap>=0) ad = a[ap--] == '1';
            if(bp>=0) bd = b[bp--] == '1';
          
            out = static_cast<char>(ad^bd^carry + '0') + out;
            carry = ad+bd+carry >> 1;
            
        }
        
        return out;


    }
        
};
