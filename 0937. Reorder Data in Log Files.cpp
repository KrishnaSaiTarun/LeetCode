class Solution {
public:
    vector<string> reorderLogFiles(vector<string>& logs) { 
        
        queue<string> digits;
        vector<string> letter;
        
        for(int i=0; i<logs.size(); i++){
            int part = logs[i].find(" ");
            if(isalpha(logs[i][part+1])){
            string s1 = logs[i].substr(part + 1, logs[i].length()-1);
            string s2 = logs[i].substr(0, part);
            s1.append(" ").append(s2);
            letter.push_back(s1);
            }
            else
                digits.push(logs[i]);
        }
        
        sort(letter.begin(), letter.end());
        
        for(int i=0; i<letter.size(); i++){
            int cut = letter[i].find_last_of(" ");
            string s1 = letter[i].substr(cut+1, letter[i].length()-1);
            string s2 = letter[i].substr(0, cut);
            letter[i] = s1.append(" ").append(s2);
        }
        
        while(!digits.empty()){
            letter.push_back(digits.front());
            digits.pop();
        }
 
        return letter;

    }
};
