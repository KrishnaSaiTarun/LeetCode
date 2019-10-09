class LRUCache {
    
    private:
    
    list<pair<int, int>> cache;
    unordered_map<int, list<pair<int,int>>::iterator> m;
    int capacity;
    
    public:
    
    LRUCache(int capacity): capacity(capacity){}  
    
    int get(int key) {
        
        if(m.find(key) != m.end()) {
            
            cache.splice(cache.begin(), cache, m[key]);
            return m[key]->second; 
            
        }
        
        return -1;
        
    } 
    
    void put(int key, int value){
        
        if(m.find(key) != m.end()){
            
            m[key]->second = value;
            cache.splice(cache.begin(), cache, m[key]);
            return;
            
        }
        
        if(m.size() == capacity){
            
            int key_to_del = cache.back().first;
            cache.pop_back();
            m.erase(key_to_del);
            
        }
        
        cache.emplace_front(key,value);
        m[key] = cache.begin();
    }
    
    
};
