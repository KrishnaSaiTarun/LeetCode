class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        
        vector<int> task(26,0);
        
        for(char c: tasks)            
            task[ c - 'A']++;
        
        sort(task.begin(), task.end());
        
        int max_val = task[25] - 1, idle = max_val * n;
        
        for(int i = 24; i>=0; i--){
                
            if(task[i] == 0) break;
            idle -= min(task[i], max_val);
            if(idle <= 0) return tasks.size(); 
            
        }
        
        return idle + tasks.size();
        
        
    }
};
