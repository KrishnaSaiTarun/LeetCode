class Solution {
public:
    
    void nextPermutation(vector<int>& nums) {
        
        int len = nums.size();
        int swap_point = -1;
        int r = len -1;
        
        while(r > 0 && nums[r] <= nums[r-1]) r--;
        
        int f_dec = r-1;
        if(f_dec<0)
            return reverse(nums, 0, len-1);
        
        while(r < len && nums[f_dec] < nums[r]) r++;
        
        swap_point = r-1;
        swap(nums, f_dec, swap_point);
        
        
        reverse(nums, f_dec+1, len-1);
     
    }
    
    void reverse(vector<int> &nums, int a, int b){
        
        while(a<b){
            
            swap(nums, a, b);
            a++; b--;
        }

       
    }
    
    void swap(vector<int> &nums, int a, int b){
        
        int temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
    }
     
    
};
