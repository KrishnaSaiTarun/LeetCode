class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        
        int sum = 0;
        int max_num = INT_MIN;
        int ans = 0;
        
        for(int i=0; i<nums.size();i++){
            
            max_num = nums[i] > max_num? nums[i]:max_num;
            sum += nums[i];
            ans = max(sum, ans);
            sum = sum<0?0:sum;
        
        }
        
        
        return max_num>0?ans:max_num;
        
    }
};
