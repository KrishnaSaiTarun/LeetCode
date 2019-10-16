class FreqStack {
public:
    
    priority_queue<tuple<int,int,int>> q;
    map<int,int> freq;
    int t;
    
    FreqStack() {
        t = 0;    
    }
    
    void push(int x) {
        q.push({++freq[x], t++, x});
    }
    
    int pop() {
        int ret = get<2>(q.top());
        q.pop();
        freq[ret]--;
        return ret;
    }
};

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack* obj = new FreqStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 */
