class Solution:
    def climbStairs(self, n: int) -> int:
        n1 = 0
        n2 = 1
        ways = 0
        for i in range(n):
            ways = ways + n1
            n3 = n1 + n2
            n1 = n2
            n2 = n3

        return ways+1 
