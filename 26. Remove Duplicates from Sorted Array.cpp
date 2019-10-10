class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int s = nums.size();
        if(s==0) return 0;
        int i = 0;
        
        for(int j = 1; j<s; j++){
            
            if(nums[j]!=nums[i]){ 
                
                i++;
                nums[i] = nums[j];
            }
        }
        
        return i+1;
        

        
    }
};
