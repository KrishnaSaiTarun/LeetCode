class Solution {
public: 
    int operation(int a, int b, string op){
        if(op == "+")
            return a+b;
        if(op == "-")
            return a-b;
        if(op == "*")
            return a*b;
        else
            return a/b;
    }
    
    bool isValidOp(string c){
        if(c == "+" || c == "-" || c == "*" || c == "/")
        return true;
        
        return false;
    }
    
    int evalRPN(vector<string>& tokens) {
        stack<int> s;

        for(int i = 0; i<tokens.size(); i++){
            string c = tokens[i];
            if(isValidOp(c)){
                if (s.size() < 2) return -1;
                int b = s.top();
                s.pop();
                int a = s.top();
                s.pop(); 
                s.push(operation(a,b,c));
            }
            else{
                s.push(stoi(c));
            }
        }
   return s.top();
    }
};
