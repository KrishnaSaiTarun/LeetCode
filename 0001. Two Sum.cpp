class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        //int size = sizeof(nums)/sizeof(nums[0]);
        vector<int> ret;
        
        map<int, int> s;
        
        for(int i=0; i<nums.size(); i++){
            
            int temp = target - nums[i];
            if(s.find(temp)!=s.end()){
                
                ret.push_back(s[temp]);
                ret.push_back(i);
                //ret[0] = s[temp];
                //ret[1] = i;
                return ret;
            }
            s[nums[i]] = i;
        }
        return ret;
    }
};
