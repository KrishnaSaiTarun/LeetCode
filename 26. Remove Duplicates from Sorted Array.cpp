class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int l = nums.size();
        if(l==0)
            return 0;
        int ret = 1;

        for(int i = 1; i<l; i++){
            
            if(nums[i] == nums[i-1])
                nums[i-1]= INT_MAX;                

            else
                ret++;

        }
        sort(nums.begin(), nums.end());
        return ret;
    }
};
