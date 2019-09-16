class Solution {
public:
    int firstUniqChar(string s) {
        vector<int> a(26,0);
        for(int i=0; i<s.length(); i++)
            a[s[i] - 'a']++;
        for(int i=0; i<s.length(); i++){
            if(a[s[i] - 'a'] == 1)
            return i;
        }
        return -1;
        
       /* map<char, int> m;
        for(int i=0; i<s.length(); i++){
            if(m.find(s[i])!=m.end())
                m[s[i]] = -1;
            else
                m[s[i]] = i;
        }
        int min = INT_MAX;
        for(map<char, int>::iterator i=m.begin(); i!=m.end(); i++){
            if(i->second != -1 && i->second < min)
                min = i->second;
        }
        
        return min==INT_MAX? -1: min;*/

    }
};
