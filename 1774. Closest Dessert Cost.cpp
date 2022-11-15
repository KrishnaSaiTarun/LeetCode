class Solution(object):
    def closestCost(self, baseCosts, toppingCosts, target):
        """
        :type baseCosts: List[int]
        :type toppingCosts: List[int]
        :type target: int
        :rtype: int
        """
        """
        KST:
        We have to choose one ice cream for sure and only 1
        Toppings - think about it
        """
        
        self.possible_toppingCosts = []
        def dfs(i, running_cost):
            if i >= len(toppingCosts):
                self.possible_toppingCosts.append(running_cost)
                return 
            
            dfs(i+1, running_cost + (0 * toppingCosts[i]))
            dfs(i+1, running_cost + (1 * toppingCosts[i]))
            dfs(i+1, running_cost + (2 * toppingCosts[i]))
        
        running_cost = 0
        dfs(0, running_cost)

        ans = min_diff = float("inf")
        for ice_cream in baseCosts:
            for entry in self.possible_toppingCosts:
                
                cost = ice_cream + entry
                diff = abs(target - cost)
                if diff < min_diff:
                    min_diff = diff
                    ans = cost
                if diff == min_diff:
                    ans = min(ans, cost)      
        return ans


