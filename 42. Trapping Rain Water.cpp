class Solution {
public:
    int trap(vector<int>& height) {
        
        int len = height.size();
        int max = 0, max_i = 0;
        for(int i =0; i<len; i++){
            if(height[i]>=max){
                max = height[i];
                max_i = i;
            }
        }
        if(max == 0) return 0;
        
        
        int l = 0;
        int water = 0;
        
        // Left side of max
        for(int i=0; i<=max_i; i++){
            
            if(height[i]>=height[l]){
                l = i;
            }
            
            else{
                
                water+=height[l]-height[i];
            }
        }
               
        int r = len-1;
        // Right side of max
        for(int i = len-1; i>=max_i; i--){
            
            if(height[i]>=height[r]){
                r = i;
            }
            
            else{
                water+=height[r]-height[i];
            }
        }
        
        return water;
     
    }
};
