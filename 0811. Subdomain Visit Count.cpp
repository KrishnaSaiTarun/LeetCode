class Solution {
public:
    vector<string> subdomainVisits(vector<string>& cpdomains) {
        
        unordered_map<string, int> m;
        vector<string> ret;
        
        for(string s: cpdomains){
            
            int i = s.find(' ');
            int num = stoi(s.substr(0,i));
            int len = s.length();
            int dot1 = s.find_first_of('.');
            int dot2 = s.find_last_of('.');
            
            string sub3 = s.substr(i+1, len-(i+1));               
            m[sub3] += num;
                           
            string sub1 =  s.substr(dot1+1, len-(dot1+1));
            m[sub1] += num;
            
            if(dot2!=dot1){
                
                string sub2 = s.substr(dot2+1, len-(dot2+1));                
                m[sub2] += num;
            }       
        }
                    
        for(auto i : m)
            ret.push_back(to_string(i.second)+ ' ' + i.first);
           
        return ret;
        
    }
};
