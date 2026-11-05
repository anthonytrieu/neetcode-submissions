class Solution:
    def climbStairs(self, n: int) -> int:
        # 1d dp solution
        # 1d memoization used when the recursive function has 
        # one argument whose value changes with every fn call

        # hash map
        calculated = {}

        def dfs(n):
            if n == 0:
                return 1
            if n < 0:
                return 0
            
            # check if calculated
            if n in calculated:
                return calculated[n]
            
            one_step = dfs(n - 1)
            two_steps = dfs(n - 2)

            # store results
            calculated[n] = one_step + two_steps

            return one_step + two_steps

        return dfs(n) 
















        # brute force doing this recursively

        # base case
        # if n == 0:
        #     return 1

        # if n < 0:
        #     return 0

        # # recursive case
        # # explore taking one step
        # one_step = self.climbStairs(n - 1)

        # two_steps = self.climbStairs(n - 2)

        # return one_step + two_steps

        # time complexity is 2^n where n is the height of the recursion tree and space complexity is o(n) since we only explore one branch at a time and not both simutaneously










# other attempt

        # # hash map
        # calculated = {}

        # # base case
        # if n == 0:
        #     return 1

        # # recursion(?)
        # # we need to do recursion then store the value in calculated
        # for i in range(len(n)):
        #     if climbStairs(n) in calculated:
        #         return calculated[i]

        #     else:
        #         calculated[i] = climbStairs(n)
        #         return climbStairs(n)
        
        # return
                


