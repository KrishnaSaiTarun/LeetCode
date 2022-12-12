class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:

        n1 = len(v1)
        n2 = len(v2)

        p1 = 0
        p2 = 0

        def get_num(p, n, v) -> (int, int):
            
            if p >= n: 
                return 0, n
            
            start = p
            while p < n and v[p] != ".":
                p += 1

            return int(v[start:p]), p+1
            
            

        while p1 < n1 or p2 < n2:
            v1_num, p1 = get_num(p1, n1, v1)
            v2_num, p2 = get_num(p2, n2, v2)
            if v1_num > v2_num:
                return 1
            elif v1_num < v2_num:
                return -1
            
