using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        
        int len = nums.size();
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());
        
        for(int j = 0; j<len-2; j++){
            
            if(nums[j]>0) break;

            int l = j+1;
            int r = len-1;
            int target = 0 - nums[j];
            
            while(l<r){
                
                int sum = nums[l] + nums[r];
                if(sum == target){
                    
                    vector<int> tup{nums[j], nums[l], nums[r]};  
                    res.push_back(tup);
                    
                    while(l<r && nums[l] == nums[l+1]) l++;
                    l++;
                    
                    while(r>l && nums[r] == nums[r-1]) r--;
                    r--;
                }
                
                else if(sum < target) l++;
                
                else r--;
            }
            
            while(j<len-2 && nums[j] == nums[j+1]) j++;
        }
        
        return res;
        
    }
};
