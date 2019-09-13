// Forward declaration of ArrayReader class.
class ArrayReader;

class Solution {
public:
    int search(const ArrayReader& reader, int target) {
        int l = 0;
        if(reader.get(l) == target)
            return l;
        int r = 1;
        while(reader.get(r) <= target){
            if(reader.get(r)==target)
                return r;
            //r = r*2;
            r = r*4;
        }
        l = 1;
        //r = INT_MAX;
        while(l<=r){
            int mid = (l+r)/2;
            
            if(reader.get(mid) > target)
                r = mid -1;
            else if(reader.get(mid) < target)
                l = mid+1;
            else
                return mid; 
        }
        
        return -1;
    }
};
