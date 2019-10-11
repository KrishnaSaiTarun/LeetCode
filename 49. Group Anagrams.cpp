class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        unordered_map<string, vector<string>> m;
        
        for(string s: strs){
            
            string t = s;
            sort(s.begin(), s.end());
            m[s].push_back(t);
        }
        
        vector<vector<string>> anagrams;
        
        for(auto mp:m){
            
            vector<string> ana(mp.second.begin(), mp.second.end());
            anagrams.push_back(ana);
            
        }
        
        return anagrams;
        
    }
};
