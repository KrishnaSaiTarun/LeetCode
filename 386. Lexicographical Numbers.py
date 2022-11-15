class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        """
        KST:
        See number of digits. It matters I suppose
        1 then 10 then 100 ... DFS ....
        print then move on and then move side
        """

        ans = []
        def dfs(integer):
            if integer > n:
                return
            ans.append(integer)
            for i in range(10):
                dfs(integer*10 + i)

        
        for i in range(1,10):
            dfs(i)
        
        return ans 

