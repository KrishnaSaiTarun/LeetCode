class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        
        int l = nums.size();
        vector<int> out(l,1);
  
        for(int i = 1; i< l; i++)
            out[i] = out[i-1]*nums[i-1];
        
        int r = nums[l-1];
        for(int i = l-2; i>=0; i--){
            
            out[i] = out[i] * r;
            r = r*nums[i];
            
            }
        
        return out;
      
    }
};
