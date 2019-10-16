class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = 0;
        int r = height.size()-1;
        int answer = 0;
        while(l!=r){
            answer = max(answer, (min(height[r],height[l]) * (r-l)));
            if(height[l]>=height[r]) r--;
            else l++;
        }
        return answer;
    }
};
