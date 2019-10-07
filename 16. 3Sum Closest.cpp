class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        
        sort(nums.begin(), nums.end());
        int len = nums.size();
        int diff = INT_MAX;
        int result = 0;
        
        for(int i = 0; i<len-2; i++){
            
            int l = i+1;
            int r = len - 1;
            
            while(l<r){
                
                int sum = nums[i] + nums[l] + nums[r];
                if(abs(sum - target) < diff){
                    
                    diff = abs(sum - target);
                    result = sum;
                    if(diff == 0) return target;
                    
                }
                      
                if(sum < target) l++;
                else r--;
            }
            
            
        }
        
        return result;
        
    }
};
