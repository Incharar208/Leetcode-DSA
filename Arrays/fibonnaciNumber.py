class Solution:
    def fib(self, n: int) -> int:
        n1 = 0
        n2 = 1
        resultList = []
        for i in range(n):
            resultList.append(n1)
            n3 = n1 + n2
            n1 = n2
            n2 = n3

        return n1   
