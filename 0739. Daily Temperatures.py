    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        """
        KST: Maybe traverse back and store min Warmest and index
        """
        ans = [0] * len(temperatures)
        
        stack = []

        for i in range(len(temperatures)-1, -1, -1):

            cur_temp = temperatures[i]
            while(stack and temperatures[stack[-1]] <= cur_temp):
                stack.pop()
    
            ans[i] = stack[-1] - i if stack else 0
            stack.append(i)
        
        return ans
