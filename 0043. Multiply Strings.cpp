class Solution {
public:
    string multiply(string num1, string num2) {
        
        int l1 = num1.length();
        int l2 = num2.length();
        
        string out(l1+l2, '0');
        
        for(int i = l1-1; i>=0; i--){
            int carry = 0;
            for(int j = l2-1; j>=0; j--){
                
                int temp = (out[i+j+1] - '0') + carry + (num1[i] - '0')*(num2[j] - '0');
                out[i+j+1] = temp%10 + '0';
                carry = temp/10;
            }
            out[i] += (carry);
        }
        
             for (int i = 0; i < l1 + l2; i++) {
            if (out[i] != '0') 
                return out.substr(i);
        } 
        return "0";
    }
   
};
