class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        
        vector<int> out;
        
        int len = numbers.size();
        
        int i = 0;
        int r = len-1;
        
        while(i<r){
            
            if(numbers[i]+numbers[r] > target) {
                
                while(i<r && numbers[r-1] == numbers[r])
                r--;
                
                r--;
            }
            
            else if(numbers[i] + numbers[r] < target) {
                
                while(i<r && numbers[i+1] == numbers[i])
                i++;
                
                i++;
            }
            
            else{
                out.push_back(i+1);
                out.push_back(r+1);
                return out;
            }
        }
        
        return out;
        
    }
};
