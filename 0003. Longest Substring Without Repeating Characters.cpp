class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        unordered_map<char, int> m;
        int len = s.length();
        int l = 0;
        int r = 0;
        int ans = 0;
        
        while(r!= len){
            
            if(m.find(s[r]) != m.end())
               l = max(m[s[r]] + 1, l); 
     
            ans = max(r - l + 1, ans);
            m[s[r]] = r;
            r++;
        }
        
        return ans;
        
    }
};
