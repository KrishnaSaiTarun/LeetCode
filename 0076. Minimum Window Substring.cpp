class Solution {
public:
    string minWindow(string s, string t) {
        
        int sl = s.length();
        int count = t.length();
        
        if(count> sl || sl == 0 || count == 0) return "";
        
        vector<int> rem(128,0);        
        
        for(int i=0; i<count; i++) rem[t[i]]++;
        
        int min = INT_MAX, l = 0, r = 0, start = 0;
        
        while(l<sl && r<=sl){
            
            if(count){
                if(r == sl)
                    break;
                rem[s[r]]--;
                if(rem[s[r]]>=0) count--;
                r++;
            }
            
            else{
                
                if(r-l<min){
                    min = r-l;
                    start = l;
                }
                rem[s[l]]++;
                if(rem[s[l]] > 0) count++;
                l++;
            }
            
            
        }return min == INT_MAX? "":s.substr(start, min);
        
    }
};
